# Copyright 2024 - GitHub user: fredericks1982

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module manages the HTTP interaction with the Came Domotic API.

Note:
   As a consumer of the CAME Domotic Unofficial library, **it's quite unlikely that you
   will need to use this class directly**: you should use the ``CameDomoticAPI`` and the
   CameEntity classes instead.

   In case of special needs, consider requesting the implementation of the desired
   feature in the Came Domotic Unofficial library, or forking the library and implement
   the feature yourself.
"""


from datetime import datetime, timezone, timedelta
import json
from typing import Optional
import requests
from aiohttp import ClientSession, ClientResponse
from .errors import (
    CameDomoticAuthError,
    CameDomoticServerError,
    CameDomoticServerNotFoundError,
)


class Auth:
    """Class to make authenticated requests to the CAME Domotic API server."""

    def __init__(
        self, websession: ClientSession, host: str, username: str, password: str
    ):
        """Initialize the Auth instance.

        Args:
            websession (ClientSession): the aiohttp client session.
            host (str): the host of the Came Domotic server.
            username (str): the username to use for the authentication.
            password (str): the password to use for the authentication.

        Raises:
            CameDomoticServerNotFoundError: if the server is not available

        Note:
            The session is not logged in until the first request is made.
        """
        self.websession = websession
        self.host = host
        self.username = username
        self.password = password

        self.session_expiration_timestamp = datetime(2000, 1, 1, tzinfo=timezone.utc)

        self.client_id = ""
        self.keep_alive_timeout_sec = 0
        self.cseq = 0

        try:
            self.validate_host()
        except requests.RequestException as e:
            raise CameDomoticServerNotFoundError(f"Server '{host}' not found") from e

    # region Context manager

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.async_dispose()

    # endregion

    def get_endpoint_url(self) -> str:
        """Get the CAME Domotic endpoint URL.

        Returns:
            str: the endpoint URL.
        """

        return f"http://{self.host}/domo/"

    @staticmethod
    def get_http_headers() -> dict:
        """Provide the default HTTP headers to use in the requests.

        Returns:
            dict: the HTTP headers.
        """

        return {
            "Content-Type": "application/x-www-form-urlencoded",
            "Connection": "Keep-Alive",
        }

    async def async_get_valid_client_id(self) -> str:
        """Get a valid client ID, eventually logging in if needed.

        Returns:
            str: the client ID.

        Raises:
            CameDomoticAuthError: if an error occurs during the login.
        """

        if not self.validate_session():
            await self.async_login()
        return self.client_id

    async def async_send_command(
        self, payload: dict, timeout: Optional[int] = 10
    ) -> ClientResponse:
        """Send a command to the Came Domotic server.

        Args:
            payload (dict): the payload to send.
            timeout (int, optional): the timeout in seconds (default: 10s).

        Returns:
            ClientResponse: the response.

        Raises:
            CameDomoticServerError: if an error occurs during the command.
        """

        try:
            response = await self.websession.post(
                self.get_endpoint_url(),
                data={"command": json.dumps(payload)},
                headers=self.get_http_headers(),
                timeout=timeout,
            )
        except Exception as e:
            raise CameDomoticServerError("Error sending command.") from e

        # Check if the response HTTP status is 2xx
        if 200 <= response.status < 300:
            # Increment the command sequence number
            self.cseq += 1
            # Refresh the session expiration timestamp, keeping 30 secs of "safe zone"
            self.session_expiration_timestamp = datetime.now(timezone.utc) + timedelta(
                seconds=max(0, self.keep_alive_timeout_sec - 30)
            )

        await self.async_raise_for_status_and_ack(response)

        return response

    # The following method is not async because it is used in the __init__ method
    def validate_host(self, timeout: Optional[int] = 10):
        """Validate the host.

        Args:
            timeout (int, optional): the timeout in seconds (default: 10s).

        Raises:
            requests.RequestException: if an error occurs during the request.
        """
        # Use the "requests" library (sync) to check if the server is available
        with requests.get(
            self.get_endpoint_url(),
            timeout=timeout,
        ) as resp:
            # Ensure that the server URL is available
            resp.raise_for_status()
            if resp.status_code != 200:
                raise requests.HTTPError(f"HTTP error {resp.status_code}.")

    async def async_login(self) -> None:
        """Login to the Came Domotic server.

        Raises:
            CameDomoticAuthError: if an error occurs during the login.
        """

        payload = {
            "sl_cmd": "sl_registration_req",
            "sl_login": self.username,
            "sl_pwd": self.password,
        }

        try:
            response = await self.async_send_command(payload)
            data = await response.json(content_type=None)
            self.client_id = data.get("sl_client_id")
            self.keep_alive_timeout_sec = data.get("sl_keep_alive_timeout_sec")
        except Exception as e:
            raise CameDomoticAuthError("Generic error logging in") from e

        self.session_expiration_timestamp = datetime.now(timezone.utc) + timedelta(
            seconds=max(0, self.keep_alive_timeout_sec - 30)
        )

    async def async_keep_alive(self) -> None:
        """Keep the session alive, eventually logging in again if needed.

        Raises:
            CameDomoticServerError: if an error occurs during the keep-alive.
            CameDomoticAuthError: if an error occurs during the login.
        """

        if not self.validate_session():
            await self.async_login()
        else:
            payload = {
                "sl_client_id": self.client_id,
                "sl_cmd": "sl_keep_alive_req",
            }
            await self.async_send_command(payload)

    async def async_logout(self) -> None:
        """Logout from the Came Domotic server.

        Raises:
            CameDomoticServerError: if an error occurs during the logout.
        """

        # Logout only if the session is still valid
        if self.validate_session():
            payload = {
                "sl_client_id": self.client_id,
                "sl_cmd": "sl_logout_req",
            }
            await self.async_send_command(payload)
            self.client_id = ""
            self.session_expiration_timestamp = datetime.now(timezone.utc)

    async def async_dispose(self):
        """Dispose the Auth instance, eventually logging out if needed."""
        if self.validate_session():
            try:
                await self.async_logout()
            except CameDomoticServerError:
                pass
        await self.websession.close()

    # region Utilities

    def validate_session(self) -> bool:
        """Check whether the session is still valid or not."""
        return self.session_expiration_timestamp > datetime.now(timezone.utc)

    @staticmethod
    async def async_raise_for_status_and_ack(response: ClientResponse):
        """Check the response status and raise an error if necessary.

        Args:
            response (ClientResponse): the response.

        Raises:
            CameDomoticServerError: if there is an error interacting with
                the remote Came Domotic server.
        """
        try:
            response.raise_for_status()
        except Exception as e:
            raise CameDomoticServerError() from e

        try:
            resp_json = await response.json(content_type=None)
        except json.JSONDecodeError as e:
            raise CameDomoticServerError("Error decoding the response") from e

        ack_reason = resp_json.get("sl_data_ack_reason")

        if ack_reason and ack_reason != 0:
            raise CameDomoticServerError(f"Bad sl_data_ack_reason code: {ack_reason}")

    # endregion

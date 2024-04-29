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
This module defines the Python representation of each of the entity types used by the
CAME Domotic API.
"""

from dataclasses import dataclass
from typing import Optional

from came_domotic_unofficial.errors import CameDomoticAuthError

from .auth import Auth


class CameEntity:
    """Base class for all the CAME entities."""


class CameUser(CameEntity):
    """User configured in a CAME Domotic server."""

    def __init__(self, raw_data: dict, auth: Auth):
        """Initialize the object."""
        if raw_data is None or "name" not in raw_data:
            raise ValueError(
                "raw_data must be a dictionary, containing the 'name' key."
            )
        self.raw_data: dict = raw_data
        self.auth: Auth = auth

    async def async_set_as_current_user(self, password: str):
        """Set the user as the current user in the CAME Domotic API session.

        Args:
            password (str): Password of the user.

        Raises:
            CameDomoticAuthError: If the authentication fails.

        Note:
            This method logs out the current user and logs in with the new user.
            In case of failure, the previous user is restored.
        """

        # Logout the current user
        backup_name = self.auth.username
        backup_pwd = self.auth.password
        await self.auth.async_logout()

        try:
            # Login with the new user
            self.auth.username = self.name
            self.auth.password = password
            await self.auth.async_login()
        except CameDomoticAuthError as e:
            # If login fails, restore the previous user
            self.auth.username = backup_name
            self.auth.password = backup_pwd
            raise e

    # Note: each property name maps the name in the returned data

    @property
    def name(self) -> str:
        """Name of the user."""
        return self.raw_data["name"]


@dataclass
class CameFeature(CameEntity):
    """Feature of a CAME domotic server."""

    name: str
    """
    Name of the feature.
    
    Known values (as of now) are:
        - "lights"
        - "openings"
        - "thermoregulation"
        - "scenarios"
        - "digitalin"
        - "energy"
        - "loadsctrl"
    """


@dataclass
class CameServerInfo(CameEntity):
    """Server information of a CAME Domotic server."""

    keycode: str
    """Keycode of the server (i.e. MAC address in the form 001122AABBCC)."""

    serial: str
    """Serial number of the server."""

    swver: Optional[str] = None
    """Software version of the server."""

    type: Optional[str] = None
    """Type of the server."""

    board: Optional[str] = None
    """Board type of the server."""


class CameLight(CameEntity):
    """Light entity in the CameDomotic API."""

    def __init__(self, raw_data: dict, auth: Auth):
        """Initialize the object."""
        self.raw_data: dict = raw_data
        self.auth: Auth = auth

    # Note: each property name maps the name in the returned data

    @property
    def act_id(self) -> int:
        """ID of the light."""
        return self.raw_data["act_id"]

    @property
    def floor_ind(self) -> int:
        """Floor index of the light."""
        return self.raw_data["floor_ind"]

    @property
    def name(self) -> str:
        """Name of the light."""
        return self.raw_data["name"]

    @property
    def room_ind(self) -> int:
        """Room index of the light."""
        return self.raw_data["room_ind"]

    @property
    def status(self) -> int:
        """Status of the light. Allowed values are 1 (ON) and 0 (OFF)."""
        return self.raw_data["status"]

    @property
    def type(self) -> str:
        """
        Light type. Allowed values are "STEP_STEP" (normal lights) and "DIMMER"
        (dimmable lights).
        """
        return self.raw_data["type"]

    @property
    def perc(self) -> int:
        """
        Brightness percentage of the light (range 0-100).
        Non dimmable lights will always return 100.
        """
        return self.raw_data.get("perc", 100)

    async def async_set_status(self, status: int, brightness: Optional[int] = None):
        """Control the light.

        Args:
            status (int): Status of the light (1 - ON, 0 - OFF).
            brightness (Optional[int]): Brightness percentage of the light (range
                0-100). This argument is ignored for non-dimmable lights.

        Raises:
            CameDomoticAuthError: If the authentication fails.
            CameDomoticServerError: If the server returns an error.
        """

        client_id = await self.auth.async_get_valid_client_id()
        payload = {
            "sl_appl_msg": {
                "act_id": self.act_id,
                "client": client_id,
                "cmd_name": "light_switch_req",
                "cseq": self.auth.cseq + 1,
                "wanted_status": status,
                # "perc": 80, # added conditionally by the logic below
            },
            "sl_appl_msg_type": "domo",
            "sl_client_id": client_id,
            "sl_cmd": "sl_data_req",
        }

        if isinstance(brightness, int) and self.type == "DIMMER":
            uploading_brightness = True
            normalized_brightness = max(0, min(brightness, 100))
            payload["sl_appl_msg"]["perc"] = normalized_brightness  # type: ignore
        else:
            uploading_brightness = False

        await self.auth.async_send_command(payload)

        # Update the status of the light if everything went as expected
        self.raw_data["status"] = status
        if uploading_brightness:
            self.raw_data["perc"] = normalized_brightness


# Openings
# Scenarios
# Digital inputs

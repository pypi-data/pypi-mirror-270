import json

import shv

from typing import Optional, Literal

from ..node._node import (
    SHVNode,
    SHVPropertyNode,
    SHVPropertySetterNode,
    SHVDigitalOutputTestNode
)


def generate_request_message(
    vehicle_id: int,
    route_code: Optional[int] = None,
    line_number: Optional[int] = None,
    service_number: Optional[int] = None,
    direction: Literal["N", "R", "L", "S"] | None = None,
    side: Literal["R_2ND", "F_2ND", "R_1ST", "F_1ST", "F", "R"] | None = None,
    ready_to_start: Optional[int] = None,  # any number
    vehicle_type: Literal[1, 2, 3, 4, 8, 32, 40, 48, 56, 60, 99] | None = None,
    category: Literal[0, 2, 3] | None = None,
    stand: Literal[0, 1] | None = None
) -> str:
    """Generate a request message for the requestor test nodes.

    For the "direction" and "side" parameters, specific string values are
    expected. Parameters "vehicle_id", "line_number", "route_code", and
    "service_number" are expected to be integers. The "ready_to_start"
    parameter can be any number (the function only checks for its presence).
    For other parameters, integer values corresponding to their enum values
    are expected. See the System G3 Core wiki pages for more information
    about the parameters needed for each requestor and the values they expect.

    Note that not all parameters are needed for all requestor test nodes.
    Provided parameters that are not needed for a specific requestor test node
    will be ignored. Parameters that are not provided will not be included
    in the request message.

    Examples:

    >>> generate_request_message(vehicle_id=123, direction="R", side="F_1ST")
    '{"vehicleId": 123, "direction": "R", "side": "F_1ST"}'

    Args:
        vehicle_id (int): The vehicle ID. This is the only mandatory\
            parameter (filling it in activates the communication).
        route_code (Optional[int], optional): The route code.\
            Defaults to None.
        line_number (Optional[int], optional): The line number.\
            Defaults to None.
        service_number (Optional[int], optional): The service number.\
            Defaults to None.
        direction (str | None, optional): The direction enum value.\
            If not provided, is not used by default. For the DRR requestor,\
            if "side" is not set to "F_1ST" or "F", direction is reset to 0\
            when the request message is processed. Defaults to None.
        side (str | None, optional): The side enum value.\
            If not provided, is considered to be "F_1ST". Defaults to None.
        ready_to_start (Optional[int], optional): Any number (function only\
            checks for presence of this parameter). Defaults to None.
        vehicle_type (Optional[int], optional): The vehicle type enum value.\
            If not provided, is considered to be 32. For the Vecom requestor,\
            if "side" is not set to "F_1ST" or "F", vehicle type is set to 8\
            when the request message is processed. Defaults to None.
        category (Optional[int], optional): The category enum value.\
            If not provided, is not used by default. Defaults to None.
        stand (Optional[int], optional): The stand enum value.\
            If not provided, is not used by default. Defaults to None.

    Returns:
        str: The request message as a JSON string.
    """
    data: dict[str, str | int] = {"vehicleId": vehicle_id}
    if route_code is not None:
        data["routeCode"] = route_code
    if line_number is not None:
        data["lineNumber"] = line_number
    if service_number is not None:
        data["serviceNumber"] = service_number
    if direction is not None:
        data["direction"] = direction
    if side is not None:
        data["side"] = side
    if ready_to_start is not None:
        data["readyToStart"] = ready_to_start
    if vehicle_type is not None:
        data["vehicleType"] = vehicle_type
    if category is not None:
        data["category"] = category
    if stand is not None:
        data["stand"] = stand
    return json.dumps(data)


###############################################################################
# DIGITAL (KEY SWITCH)
###############################################################################

class SHVKeySwitchButtonTestNode(SHVDigitalOutputTestNode):
    pass


class SHVKeySwitchTestNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.buttons: dict[str, SHVKeySwitchButtonTestNode] = {}
        """Key switch buttons nodes."""


###############################################################################
# VECOM
###############################################################################

class SHVVecomLoopTestNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.error = SHVPropertyNode(path=f'{path}/error')
        """[BOOL] Communication error."""
        self.cmd_to_tram = SHVPropertyNode(path=f'{path}/cmdToTram')
        """[UINT] Command sent by Vecom loop to a tram."""
        self.loop = SHVPropertySetterNode(path=f'{path}/loop')
        """[INT] Loop number (from 1 to 8)."""

    async def reset(self, **kwargs) -> shv.SHVType:
        """Reset Vecom loop (tram data and loop number)."""
        return await self.call('reset', **kwargs)

    async def reset_tram(self, **kwargs) -> shv.SHVType:
        """Reset all tram data, set tram communication inactive."""
        return await self.call('resetTram', **kwargs)

    async def new_tram_data(self, request: str, **kwargs) -> shv.SHVType:
        """Set the new tram data, set tram communication active (over loop)."""
        if 'param' in kwargs:
            del kwargs['param']
        return await self.call('newTramData', param=request, **kwargs)


###############################################################################
# DRR
###############################################################################

class SHVDRRTransceiverTestNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.error = SHVPropertyNode(path=f'{path}/error')
        """[BOOL] Communication error."""
        self.channel = SHVPropertySetterNode(path=f'{path}/channel')
        """[INT] Channel number (from 1 to 4)."""

    async def reset(self, **kwargs) -> shv.SHVType:
        """Reset DRR transceiver (tram data and channel)."""
        return await self.call('reset', **kwargs)

    async def reset_tram(self, **kwargs) -> shv.SHVType:
        """Reset all tram data, set tram communication inactive."""
        return await self.call('resetTram', **kwargs)

    async def new_tram_data(self, request: str, **kwargs) -> shv.SHVType:
        """Set the new tram data, set tram communication active (over loop)."""
        if 'param' in kwargs:
            del kwargs['param']
        return await self.call('newTramData', param=request, **kwargs)


###############################################################################
# SPIE
###############################################################################

class SHVSPIELoopTestNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.error = SHVPropertyNode(path=f'{path}/error')
        """[BOOL] Communication error."""
        self.loop = SHVPropertySetterNode(path=f'{path}/loop')
        """[INT] Channel number (from 1 to 12)."""

    async def reset(self, **kwargs) -> shv.SHVType:
        """Reset SPIE loop (tram data and channel)."""
        return await self.call('reset', **kwargs)

    async def reset_tram(self, **kwargs) -> shv.SHVType:
        """Reset all tram data, set tram communication inactive."""
        return await self.call('resetTram', **kwargs)

    async def new_tram_data(self, request: str, **kwargs) -> shv.SHVType:
        """Set the new tram data, set tram communication active (over loop)."""
        if 'param' in kwargs:
            del kwargs['param']
        return await self.call('newTramData', param=request, **kwargs)


###############################################################################
# VETRA
###############################################################################

class SHVVetraTestNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.error = SHVPropertyNode(path=f'{path}/error')
        """[BOOL] Communication error."""
        self.address = SHVPropertySetterNode(path=f'{path}/address')
        """[INT] Vetra address (-1 if not used)."""

    async def reset(self, **kwargs) -> shv.SHVType:
        """Reset Vetra (tram data and address)."""
        return await self.call('reset', **kwargs)

    async def reset_tram(self, **kwargs) -> shv.SHVType:
        """Reset all tram data, set tram communication inactive."""
        return await self.call('resetTram', **kwargs)

    async def new_tram_data(self, request: str, **kwargs) -> shv.SHVType:
        """Set the new tram data, set tram communication active (over loop)."""
        if 'param' in kwargs:
            del kwargs['param']
        return await self.call('newTramData', param=request, **kwargs)


###############################################################################
# AWA
###############################################################################

class SHVAWATestNode(SHVNode):

    async def reset(self, **kwargs) -> shv.SHVType:
        """Reset AWA loop (all digital outputs)."""
        return await self.call('reset', **kwargs)

    async def set_left(self, **kwargs) -> shv.SHVType:
        """Send command to the LEFT (pulse 100ms)."""
        return await self.call('setLeft', **kwargs)

    async def set_straight(self, **kwargs) -> shv.SHVType:
        """Send command STRAIGHT (pulse 100ms)."""
        return await self.call('setStraight', **kwargs)

    async def set_right(self, **kwargs) -> shv.SHVType:
        """Send command to the RIGHT (pulse 100ms)."""
        return await self.call('setRight', **kwargs)

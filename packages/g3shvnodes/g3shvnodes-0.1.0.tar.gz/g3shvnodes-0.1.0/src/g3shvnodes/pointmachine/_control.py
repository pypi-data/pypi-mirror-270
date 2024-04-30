import enum

import shv

from ..node._node import (
    SHVNode,
    SHVPropertyNode,
    SHVPropertySetterNode,
    SHVStatusNode,
)


###############################################################################
# POINT MACHINE - PMM
###############################################################################

class SHVPMMStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        LEFT = 1 << 0
        """
        Point machine is switched to the left.
        """
        RIGHT = 1 << 1
        """
        Point machine is switched to the right.
        """
        MIDDLE = 1 << 2
        """
        Point machine is neither in position left nor in position right.
        """
        LEVER_IN_SOCKET = 1 << 5
        """
        Lever for manual switching is in the point machine's socket.
        """
        ERROR_INPUT_OUTPUT = 1 << 29
        """
        Hardware input or output error
        (only for devices connected to safety hardware modules).
        """
        ERROR_POSITION = 1 << 30
        """
        Point machine position error.
        Sensors on both sides of the point machine are active at the same time.
        """

    class BitMask(enum.IntFlag):
        POSITION = (1 << 0) + (1 << 1) + (1 << 2) + (1 << 30)
        """
        Point machine position (left / right / middle / error).
        """
        LEVER_IN_SOCKET = 1 << 5
        """
        Lever for manual switching is in the point machine's socket.
        """
        ERROR_INPUT_OUTPUT = 1 << 29
        """
        Hardware input or output error
        (only for devices connected to safety hardware modules).
        """
        ERROR_POSITION = 1 << 30
        """
        Point machine position error.
        Sensors on both sides of the point machine are active at the same time.
        """

    @classmethod
    def is_left(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.LEFT,
            mask=cls.BitMask.POSITION
            )

    @classmethod
    def is_right(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.RIGHT,
            mask=cls.BitMask.POSITION
            )

    @classmethod
    def is_middle(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.MIDDLE,
            mask=cls.BitMask.POSITION
            )

    @classmethod
    def is_lever_in_socket(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.LEVER_IN_SOCKET,
            mask=cls.BitMask.LEVER_IN_SOCKET
            )

    @classmethod
    def is_error_input_output(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_INPUT_OUTPUT,
            mask=cls.BitMask.ERROR_INPUT_OUTPUT
            )

    @classmethod
    def is_error_position(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_POSITION,
            mask=cls.BitMask.ERROR_POSITION
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.LEFT: cls.is_left(status),
            cls.BitAlias.RIGHT: cls.is_right(status),
            cls.BitAlias.MIDDLE: cls.is_middle(status),
            cls.BitAlias.LEVER_IN_SOCKET: cls.is_lever_in_socket(status),
            cls.BitAlias.ERROR_INPUT_OUTPUT: cls.is_error_input_output(status),
            cls.BitAlias.ERROR_POSITION: cls.is_error_position(status)
            }


class SHVPMMControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVPMMStatusNode(path=f'{path}/status')
        """[DWORD] Point machine status."""


###############################################################################
# POINT MACHINE - PME
###############################################################################

class SHVPMEStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        LEFT = 1 << 0
        """
        Point machine is switched to the left.
        """
        RIGHT = 1 << 1
        """
        Point machine is switched to the right.
        """
        MIDDLE = 1 << 2
        """
        Point machine is neither in position left nor in position right.
        """
        BLOCKED = 1 << 4
        """
        Point machine is electricaly blocked from switching
        by the control logic.
        """
        LEVER_IN_SOCKET = 1 << 5
        """
        Lever for manual switching is in the point machine's socket.
        """
        MOTOR_MOVING = 1 << 8
        """
        Point machine is currently moving (motor is active).
        """
        FLOOD_EL = 1 << 13
        """
        Electrical part of point machine is flooded.
        """
        FLOOD_MECH = 1 << 14
        """
        Mechanical part of point machine is flooded.
        """
        WARNING_POSITION_NOT_CHANGED = 1 << 15
        """
        Point machine position has not been changed during last attempt
        to switch.
        """
        FORCED_TRAILING = 1 << 16
        """
        Point machine has been force-trailed (moved from position against
        the locking mechanism). Cleared by a subsequent correct switching.
        """
        ELECTRICAL_COVER_OPEN = 1 << 17
        """
        Electrical part of point machine is cover open.
        """
        MECHANICAL_COVER_OPEN = 1 << 18
        """
        Mechanical part of point machine is cover open.
        """
        SENSOR_LEFT_01 = 1 << 19
        """
        Status of sensor L1 (raw data).
        """
        SENSOR_LEFT_02 = 1 << 20
        """
        Status of sensor L2 (raw data).
        """
        SENSOR_LEFT_03 = 1 << 21
        """
        Status of sensor L3 (raw data).
        """
        SENSOR_RIGHT_01 = 1 << 22
        """
        Status of sensor R1 (raw data).
        """
        SENSOR_RIGHT_02 = 1 << 23
        """
        Status of sensor R2 (raw data).
        """
        SENSOR_RIGHT_03 = 1 << 24
        """
        Status of sensor R3 (raw data).
        """
        ERROR_MOTOR_MOVING = 1 << 28
        """
        Point machine contactor is active despite no command
        from the control logic.
        """
        ERROR_INPUT_OUTPUT = 1 << 29
        """
        Hardware input or output error
        (only for devices connected to safety hardware modules).
        """
        ERROR_POSITION = 1 << 30
        """
        Point machine position error.
        Sensors on both sides of the point machine are active at the same time.
        """

    class BitMask(enum.IntFlag):
        POSITION = (1 << 0) + (1 << 1) + (1 << 2) + (1 << 30)
        """
        Point machine position (left / right / middle / error)
        """
        BLOCKED = 1 << 4
        """
        Point machine is electricaly blocked from switching
        by the control logic.
        """
        LEVER_IN_SOCKET = 1 << 5
        """
        Lever for manual switching is in the point machine's socket.
        """
        MOTOR_MOVING = 1 << 8
        """
        Point machine is currently moving (motor is active).
        """
        FLOOD_EL = 1 << 13
        """
        Electrical part of point machine is flooded.
        """
        FLOOD_MECH = 1 << 14
        """
        Mechanical part of point machine is flooded.
        """
        WARNING_POSITION_NOT_CHANGED = 1 << 15
        """
        Point machine position has not been changed during last attempt
        to switch.
        """
        FORCED_TRAILING = 1 << 16
        """
        Point machine has been force-trailed (moved from position against
        the locking mechanism). Cleared by a subsequent correct switching.
        """
        ELECTRICAL_COVER_OPEN = 1 << 17
        """
        Electrical part of point machine is cover open.
        """
        MECHANICAL_COVER_OPEN = 1 << 18
        """
        Mechanical part of point machine is cover open.
        """
        SENSOR_LEFT_01 = 1 << 19
        """
        Status of sensor L1 (raw data).
        """
        SENSOR_LEFT_02 = 1 << 20
        """
        Status of sensor L2 (raw data).
        """
        SENSOR_LEFT_03 = 1 << 21
        """
        Status of sensor L3 (raw data).
        """
        SENSOR_RIGHT_01 = 1 << 22
        """
        Status of sensor R1 (raw data).
        """
        SENSOR_RIGHT_02 = 1 << 23
        """
        Status of sensor R2 (raw data).
        """
        SENSOR_RIGHT_03 = 1 << 24
        """
        Status of sensor R3 (raw data).
        """
        ERROR_MOTOR_MOVING = 1 << 28
        """
        Point machine contactor is active despite no command
        from the control logic.
        """
        ERROR_INPUT_OUTPUT = 1 << 29
        """
        Hardware input or output error
        (only for devices connected to safety hardware modules).
        """
        ERROR_POSITION = 1 << 30
        """
        Point machine position error.
        Sensors on both sides of the point machine are active at the same time.
        """

    @classmethod
    def is_left(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.LEFT,
            mask=cls.BitMask.POSITION
            )

    @classmethod
    def is_right(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.RIGHT,
            mask=cls.BitMask.POSITION
            )

    @classmethod
    def is_middle(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.MIDDLE,
            mask=cls.BitMask.POSITION
            )

    @classmethod
    def is_blocked(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.BLOCKED,
            mask=cls.BitMask.BLOCKED
            )

    @classmethod
    def is_lever_in_socket(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.LEVER_IN_SOCKET,
            mask=cls.BitMask.LEVER_IN_SOCKET
            )

    @classmethod
    def is_motor_moving(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.MOTOR_MOVING,
            mask=cls.BitMask.MOTOR_MOVING
            )

    @classmethod
    def is_flood_el(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.FLOOD_EL,
            mask=cls.BitMask.FLOOD_EL
            )

    @classmethod
    def is_flood_mech(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.FLOOD_MECH,
            mask=cls.BitMask.FLOOD_MECH
            )

    @classmethod
    def is_warning_position_not_changed(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.WARNING_POSITION_NOT_CHANGED,
            mask=cls.BitMask.WARNING_POSITION_NOT_CHANGED
            )

    @classmethod
    def is_forced_trailing(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.FORCED_TRAILING,
            mask=cls.BitMask.FORCED_TRAILING
            )

    @classmethod
    def is_electrical_cover_open(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ELECTRICAL_COVER_OPEN,
            mask=cls.BitMask.ELECTRICAL_COVER_OPEN
            )

    @classmethod
    def is_mechanical_cover_open(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.MECHANICAL_COVER_OPEN,
            mask=cls.BitMask.MECHANICAL_COVER_OPEN
            )

    @classmethod
    def is_sensor_left_01(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.SENSOR_LEFT_01,
            mask=cls.BitMask.SENSOR_LEFT_01
            )

    @classmethod
    def is_sensor_left_02(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.SENSOR_LEFT_02,
            mask=cls.BitMask.SENSOR_LEFT_02
            )

    @classmethod
    def is_sensor_left_03(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.SENSOR_LEFT_03,
            mask=cls.BitMask.SENSOR_LEFT_03
            )

    @classmethod
    def is_sensor_right_01(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.SENSOR_RIGHT_01,
            mask=cls.BitMask.SENSOR_RIGHT_01
            )

    @classmethod
    def is_sensor_right_02(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.SENSOR_RIGHT_02,
            mask=cls.BitMask.SENSOR_RIGHT_02
            )

    @classmethod
    def is_sensor_right_03(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.SENSOR_RIGHT_03,
            mask=cls.BitMask.SENSOR_RIGHT_03
            )

    @classmethod
    def is_error_motor_moving(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_MOTOR_MOVING,
            mask=cls.BitMask.ERROR_MOTOR_MOVING
            )

    @classmethod
    def is_error_input_output(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_INPUT_OUTPUT,
            mask=cls.BitMask.ERROR_INPUT_OUTPUT
            )

    @classmethod
    def is_error_position(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_POSITION,
            mask=cls.BitMask.ERROR_POSITION
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.LEFT:
                cls.is_left(status),
            cls.BitAlias.RIGHT:
                cls.is_right(status),
            cls.BitAlias.MIDDLE:
                cls.is_middle(status),
            cls.BitAlias.BLOCKED:
                cls.is_blocked(status),
            cls.BitAlias.LEVER_IN_SOCKET:
                cls.is_lever_in_socket(status),
            cls.BitAlias.MOTOR_MOVING:
                cls.is_motor_moving(status),
            cls.BitAlias.FLOOD_EL:
                cls.is_flood_el(status),
            cls.BitAlias.FLOOD_MECH:
                cls.is_flood_mech(status),
            cls.BitAlias.WARNING_POSITION_NOT_CHANGED:
                cls.is_warning_position_not_changed(status),
            cls.BitAlias.FORCED_TRAILING:
                cls.is_forced_trailing(status),
            cls.BitAlias.ELECTRICAL_COVER_OPEN:
                cls.is_electrical_cover_open(status),
            cls.BitAlias.MECHANICAL_COVER_OPEN:
                cls.is_mechanical_cover_open(status),
            cls.BitAlias.SENSOR_LEFT_01:
                cls.is_sensor_left_01(status),
            cls.BitAlias.SENSOR_LEFT_02:
                cls.is_sensor_left_02(status),
            cls.BitAlias.SENSOR_LEFT_03:
                cls.is_sensor_left_03(status),
            cls.BitAlias.SENSOR_RIGHT_01:
                cls.is_sensor_right_01(status),
            cls.BitAlias.SENSOR_RIGHT_02:
                cls.is_sensor_right_02(status),
            cls.BitAlias.SENSOR_RIGHT_03:
                cls.is_sensor_right_03(status),
            cls.BitAlias.ERROR_MOTOR_MOVING:
                cls.is_error_motor_moving(status),
            cls.BitAlias.ERROR_INPUT_OUTPUT:
                cls.is_error_input_output(status),
            cls.BitAlias.ERROR_POSITION:
                cls.is_error_position(status),
            }


class SHVPMEControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVPMEStatusNode(
            path=f'{path}/status'
            )
        """[DWORD] Point machine status."""
        self.switch_time = SHVPropertyNode(
            path=f'{path}/switchTime'
            )
        """[UDINT, ms] Last switching duration."""
        self.switch_left_counter = SHVPropertySetterNode(
            path=f'{path}/switchLeftCounter'
            )
        """[UDINT] Number of the last switching to the left."""
        self.switch_right_counter = SHVPropertySetterNode(
            path=f'{path}/switchRightCounter'
            )
        """[UDINT] Number of the last switching to the right."""
        self.switch_left_counter_permanent = SHVPropertySetterNode(
            path=f'{path}/switchLeftCounterPermanent'
            )
        """[UDINT] Total number of switchings to the left."""
        self.switch_right_counter_permanent = SHVPropertySetterNode(
            path=f'{path}/switchRightCounterPermanent'
            )
        """[UDINT] Total number of switchings to the right."""
        self.switch_forced_trailing_counter = SHVPropertySetterNode(
            path=f'{path}/switchForcedTrailingCounter'
            )
        """
        [UDINT] Forced trailing counter
        (resets after the point machine inspection).
        """

    async def switch_left(self, **kwargs) -> shv.SHVType:
        """Switch point machine to the left."""
        return await self.call("switchLeft", **kwargs)

    async def switch_right(self, **kwargs) -> shv.SHVType:
        """Switch point machine to the right."""
        return await self.call("switchRight", **kwargs)

    async def clear_switch_counter(self, **kwargs) -> shv.SHVType:
        """Reset counters after point machine inspection."""
        return await self.call("clearSwitchCounter", **kwargs)

    async def clear_switch_counter_permanent(self, **kwargs) -> shv.SHVType:
        """Reset permanent counters after point machine replacement."""
        return await self.call("clearSwitchCounterPermanent", **kwargs)

    async def clear_switch_forced_trailing_counter(self, **kwargs) -> shv.SHVType:  # noqa: E501
        """Reset forced trailing counter after point machine inspection."""
        return await self.call("clearSwitchForcedTrailingCounter", **kwargs)

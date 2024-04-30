import enum
import typing

import shv

from ..node._node import SHVNode, SHVStatusNode

if typing.TYPE_CHECKING:
    from ..gate._control import SHVGateControlNode
    from ..route._control import SHVRouteControlNode


class SHVZoneStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        UNKNOWN = 0b00
        """
        A temporary state after the system startup.
        """
        NORM = 0b01
        """
        Normal system operation.
        """
        AB = 0b10
        """
        All-Blocked state.
        """
        EI = 0b11
        """
        Emergency Inhibit state.
        """
        SAR = 1 << 8
        """
        System auto recovery is enabled or is running.
        """
        STATE_REASON_SAFETY_SYSTEM = 1 << 16
        """
        State has been set by the safety system (likely caused by an error
        of a safety peripheral module or the safety CPU itself).
        """
        STATE_REASON_CABINET_BUTTON = 2 << 16
        """
        State has been set with the hardware button from the control cabinet.
        """
        STATE_REASON_HMI_COMMAND = 3 << 16
        """
        State has been set from the HMI command panel.
        """
        STATE_REASON_DETECTOR = 4 << 16
        """
        State has been set by any detector (likely caused by an error of
        a detector).
        """
        STATE_REASON_POINT_MACHINE = 5 << 16
        """
        State has been set by any point machine (likely caused by an error of
        a point machine).
        """
        STATE_REASON_SIGNAL = 6 << 16
        """
        State has been set by any signal (likely caused by an error of
        a signal lamp).
        """
        STATE_REASON_SPAD = 8 << 16
        """
        State has been set by a SPAD (Signal Passed At Danger) event any gate.
        """
        STATE_REASON_ROUTE = 9 << 16
        """
        State has been set because of any route error (for example,
        wrong detector sequence, lost position of a point machine, etc.).
        """
        STATE_REASON_PLC_MODULE = 16 << 16
        """
        State has been set due to a PLC hardware module error.
        """
        STATE_REASON_SYSTEM_CONFIGURATION_LOADING = 17 << 16
        """
        State has been set due to the fail of the configuration loading.
        """
        STATE_REASON_UPS = 18 << 16
        """
        State has been set because the system is running from UPS battery.
        """
        STATE_REASON_SAR = 31 << 16
        """
        State has been set by the SAR (System Auto Recovery) function.
        """

    class BitMask(enum.IntFlag):
        STATE = 0b11  # bits 0-1
        """
        Zone state (NORM / AB / EI / UNKNOWN).
        """
        STATE_REASON = 0xFF0000  # bits 16-23
        """
        Zone state reason code.
        """
        SAR = 1 << 8
        """
        System auto recovery is enabled or is running.
        """

    @classmethod
    def is_unknown(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.UNKNOWN,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_norm(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.NORM,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_ab(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.AB,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_ei(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.EI,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_sar(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.SAR,
            mask=cls.BitMask.SAR
            )

    @classmethod
    def is_state_reason_initialization(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=0,
            mask=cls.BitMask.STATE_REASON
            )

    @classmethod
    def is_state_reason_safety_system(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_REASON_SAFETY_SYSTEM,
            mask=cls.BitMask.STATE_REASON
            )

    @classmethod
    def is_state_reason_cabinet_button(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_REASON_CABINET_BUTTON,
            mask=cls.BitMask.STATE_REASON
            )

    @classmethod
    def is_state_reason_hmi_command(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_REASON_HMI_COMMAND,
            mask=cls.BitMask.STATE_REASON
            )

    @classmethod
    def is_state_reason_detector(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_REASON_DETECTOR,
            mask=cls.BitMask.STATE_REASON
            )

    @classmethod
    def is_state_reason_point_machine(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_REASON_POINT_MACHINE,
            mask=cls.BitMask.STATE_REASON
            )

    @classmethod
    def is_state_reason_signal(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_REASON_SIGNAL,
            mask=cls.BitMask.STATE_REASON
            )

    @classmethod
    def is_state_reason_spad(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_REASON_SPAD,
            mask=cls.BitMask.STATE_REASON
            )

    @classmethod
    def is_state_reason_route(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_REASON_ROUTE,
            mask=cls.BitMask.STATE_REASON
            )

    @classmethod
    def is_state_reason_plc_module(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_REASON_PLC_MODULE,
            mask=cls.BitMask.STATE_REASON
            )

    @classmethod
    def is_state_reason_system_configuration_loading(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_REASON_SYSTEM_CONFIGURATION_LOADING,
            mask=cls.BitMask.STATE_REASON
            )

    @classmethod
    def is_state_reason_ups(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_REASON_UPS,
            mask=cls.BitMask.STATE_REASON
            )

    @classmethod
    def is_state_reason_sar(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_REASON_SAR,
            mask=cls.BitMask.STATE_REASON
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.UNKNOWN:
                cls.is_unknown(status),
            cls.BitAlias.NORM:
                cls.is_norm(status),
            cls.BitAlias.AB:
                cls.is_ab(status),
            cls.BitAlias.EI:
                cls.is_ei(status),
            cls.BitAlias.SAR:
                cls.is_sar(status),
            cls.BitAlias.STATE_REASON_SAFETY_SYSTEM:
                cls.is_state_reason_safety_system(status),
            cls.BitAlias.STATE_REASON_CABINET_BUTTON:
                cls.is_state_reason_cabinet_button(status),
            cls.BitAlias.STATE_REASON_HMI_COMMAND:
                cls.is_state_reason_hmi_command(status),
            cls.BitAlias.STATE_REASON_DETECTOR:
                cls.is_state_reason_detector(status),
            cls.BitAlias.STATE_REASON_POINT_MACHINE:
                cls.is_state_reason_point_machine(status),
            cls.BitAlias.STATE_REASON_SIGNAL:
                cls.is_state_reason_signal(status),
            cls.BitAlias.STATE_REASON_SPAD:
                cls.is_state_reason_spad(status),
            cls.BitAlias.STATE_REASON_ROUTE:
                cls.is_state_reason_route(status),
            cls.BitAlias.STATE_REASON_PLC_MODULE:
                cls.is_state_reason_plc_module(status),
            cls.BitAlias.STATE_REASON_SYSTEM_CONFIGURATION_LOADING:
                cls.is_state_reason_system_configuration_loading(status),
            cls.BitAlias.STATE_REASON_UPS:
                cls.is_state_reason_ups(status),
            cls.BitAlias.STATE_REASON_SAR:
                cls.is_state_reason_sar(status),
            }


class SHVZoneControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVZoneStatusNode(path=f'{path}/status')
        """[DWORD] Zone status."""
        self.gate: dict[str, 'SHVGateControlNode'] = {}
        """Gate control nodes."""
        self.route: dict[str, 'SHVRouteControlNode'] = {}
        """Route control nodes."""

    async def set_normal(self, **kwargs) -> shv.SHVType:
        """Set zone to the NORM state."""
        return await self.call('setNormal', **kwargs)

    async def set_all_blocked(self, **kwargs) -> shv.SHVType:
        """Set zone to the AB state."""
        return await self.call('setAllBlocked', **kwargs)

    async def set_all_emergency_inhibit(self, **kwargs) -> shv.SHVType:
        """Set zone to the EI state."""
        return await self.call('setEmergencyInhibit', **kwargs)

    async def test_enable_calibration(self, **kwargs) -> shv.SHVType:
        """
        Enable calibration mode (by simulating pressing the corresponding
        hardware button in the cabinet).
        """
        return await self.call('testEnableCalibration', **kwargs)

    async def test_disable_calibration(self, **kwargs) -> shv.SHVType:
        """
        Disable calibration mode (by simulating pressing the corresponding
        hardware button in the cabinet).
        """
        return await self.call('testDisableCalibration', **kwargs)

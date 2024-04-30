import enum

import shv

from ..node._node import (
    SHVNode,
    SHVPropertyNode,
    SHVPropertySetterNode,
    SHVStatusNode,
)


###############################################################################
# SIGNAL + SIGNAL SYMBOL
###############################################################################

class SHVSignalSymbolStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        STATE_OFF = 0
        """
        Symbol is switched off.
        """
        STATE_SHINING = 1
        """
        Symbol is shining permanently.
        """
        STATE_BLINKING = 2
        """
        Symbol is blinking.
        """
        STATE_ERROR = 3
        """
        Symbol is in an error state, either due to a current error (for safety
        and non-safety symbols) or an IO error (only for safety symbols).
        """
        WARNING_CURRENT_GENERAL = 1 << 24
        """
        Current is out of the acceptable deviation range for warning.
        """
        ERROR_OUTPUT = 1 << 29
        """
        Hardware output error
        (only for symbols connected to safety hardware modules).
        """
        ERROR_CURRENT = 1 << 30
        """
        Current is out of the acceptable deviation range for error or
        is lower than the minimum current limit.
        """

    class BitMask(enum.IntFlag):
        STATE = 0b11  # bits 0-1
        """Ths state of the signal symbol."""
        WARNING_CURRENT_GENERAL = 1 << 24
        """
        Current is out of the acceptable deviation range for warning.
        """
        ERROR_OUTPUT = 1 << 29
        """
        Hardware output error
        (only for symbols connected to safety hardware modules).
        """
        ERROR_CURRENT = 1 << 30
        """
        Current is out of the acceptable deviation range for error or
        is lower than the minimum current limit.
        """

    @classmethod
    def is_state_off(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_OFF,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_shining(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_SHINING,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_blinking(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_BLINKING,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_error(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_ERROR,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_warning_current_general(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.WARNING_CURRENT_GENERAL,
            mask=cls.BitMask.WARNING_CURRENT_GENERAL
            )

    @classmethod
    def is_error_output(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_OUTPUT,
            mask=cls.BitMask.ERROR_OUTPUT
            )

    @classmethod
    def is_error_current(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_CURRENT,
            mask=cls.BitMask.ERROR_CURRENT
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.STATE_OFF:
                cls.is_state_off(status),
            cls.BitAlias.STATE_SHINING:
                cls.is_state_shining(status),
            cls.BitAlias.STATE_BLINKING:
                cls.is_state_blinking(status),
            cls.BitAlias.STATE_ERROR:
                cls.is_state_error(status),
            cls.BitAlias.WARNING_CURRENT_GENERAL:
                cls.is_warning_current_general(status),
            cls.BitAlias.ERROR_OUTPUT:
                cls.is_error_output(status),
            cls.BitAlias.ERROR_CURRENT:
                cls.is_error_current(status)
            }


class SHVSignalSymbolConfigNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.current_limit_warning = SHVPropertySetterNode(
            path=f'{path}/currentLimitWarning'
            )
        """
        [INT, %] Deviation from the calibrated current
        to trigger current warning.
        """
        self.current_limit_error = SHVPropertySetterNode(
            path=f'{path}/currentLimitError'
            )
        """
        [INT, %] Deviation from the calibrated current
        to trigger current error.
        """


class SHVSignalSymbolControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVSignalSymbolStatusNode(
            path=f'{path}/status'
            )
        """[DWORD] Signal symbol status."""
        self.current_actual = SHVPropertyNode(
            path=f'{path}/currentActual'
            )
        """[REAL, mA] Actual measured current in the symbol."""
        self.current_calibrated_day = SHVPropertyNode(
            path=f'{path}/currentCalibratedDay'
            )
        """[REAL, mA] Calibrated current for a day mode."""
        self.current_calibrated_night = SHVPropertyNode(
            path=f'{path}/currentCalibratedNight'
            )
        """[REAL, mA] Calibrated current for a night mode."""
        self.config = SHVSignalSymbolConfigNode(
            path=f'{path}/config'
            )
        """Signal symbol configuration."""

    async def turn_on(self, **kwargs) -> shv.SHVType:
        """
        Turn on the test of the symbol
        (the calibration button has to be pressed in the control cabinet).
        """
        return await self.call("turnOn", **kwargs)

    async def turn_off(self, **kwargs) -> shv.SHVType:
        """Turn off the test of the symbol."""
        return await self.call("turnOff", **kwargs)


class SHVSignalStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        STATE_NIGHT_GRID = 0
        """
        Luminance sensor from the control cabinet emits signal NIGHT,
        the signal is powered from the power grid.
        """
        STATE_DAY_GRID = 1
        """
        Luminance sensor from the control cabinet emits signal DAY,
        the signal is powered from the power grid.
        """
        STATE_NIGHT_UPS = 2
        """
        Luminance sensor from the control cabinet emits signal NIGHT,
        the signal is powered from the UPS battery.
        """
        STATE_DAY_UPS = 3
        """
        Luminance sensor from the control cabinet emits signal NIGHT,
        the signal is powered from the UPS battery.
        """
        CALIBRATION_ENABLED = 1 << 8
        """
        Signal calibration procedure is enabled
        by pressing the calibration button in the control cabinet.
        """
        CALIBRATION_IN_PROGRESS = 1 << 9
        """
        Signal is currently being calibrated.
        """
        TURNED_ON_MANUALLY = 1 << 10
        """
        Signal test is running (to be switchied off by the TEST OFF button in
        the control cabinet, calibration deactivation, or after reaching
        the maximum test time of 60 minutes).
        """
        WARNING_CURRENT_GENERAL = 1 << 24
        """
        Current in any symbol of the signal is out of the warning bounds.
        """
        ERROR_IO_GENERAL = 1 << 29
        """
        Hardware error of any symbol of the signal (used only for signals
        managed by the safety software).
        """
        ERROR_CURRENT_GENERAL = 1 << 30
        """
        Current in any symbol of the signal is out of the error bounds.
        """

    class BitMask(enum.IntFlag):
        STATE = 0b11  # bits 0-1
        """
        Ths code describing the state of the signal lamp.
        """
        CALIBRATION_ENABLED = 1 << 8
        """
        Signal calibration procedure is enabled
        by pressing the calibration button in the control cabinet.
        """
        CALIBRATION_IN_PROGRESS = 1 << 9
        """
        Signal is currently being calibrated.
        """
        TURNED_ON_MANUALLY = 1 << 10
        """
        Signal test is running (to be switchied off by the TEST OFF button in
        the control cabinet, calibration deactivation, or after reaching
        the maximum test time of 60 minutes).
        """
        ASPECT = 0xFF0000  # bits 16-23
        """
        Name of the aspect (combination of symbols) shown on the signal.
        Project-specific, used only for segment signal types.
        """
        WARNING_CURRENT_GENERAL = 1 << 24
        """
        Current in any symbol of the signal is out of the warning bounds.
        """
        ERROR_IO_GENERAL = 1 << 29
        """
        Hardware error of any symbol of the signal (used only for signals
        managed by the safety software).
        """
        ERROR_CURRENT_GENERAL = 1 << 30
        """
        Current in any symbol of the signal is out of the error bounds.
        """

    @classmethod
    def is_state_day_grid(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_DAY_GRID,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_night_grid(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_NIGHT_GRID,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_day_ups(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_DAY_UPS,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_night_ups(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_NIGHT_UPS,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_calibration_enabled(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.CALIBRATION_ENABLED,
            mask=cls.BitMask.CALIBRATION_ENABLED
            )

    @classmethod
    def is_calibration_in_progress(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.CALIBRATION_IN_PROGRESS,
            mask=cls.BitMask.CALIBRATION_IN_PROGRESS
            )

    @classmethod
    def is_turned_on_manually(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.TURNED_ON_MANUALLY,
            mask=cls.BitMask.TURNED_ON_MANUALLY
            )

    @classmethod
    def is_warning_current_general(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.WARNING_CURRENT_GENERAL,
            mask=cls.BitMask.WARNING_CURRENT_GENERAL
            )

    @classmethod
    def is_error_io_general(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_IO_GENERAL,
            mask=cls.BitMask.ERROR_IO_GENERAL
            )

    @classmethod
    def is_error_current_general(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_CURRENT_GENERAL,
            mask=cls.BitMask.ERROR_CURRENT_GENERAL
            )

    @classmethod
    def aspect(cls, status: int) -> int:
        return (status & cls.BitMask.ASPECT) >> 16

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.STATE_DAY_GRID:
                cls.is_state_day_grid(status),
            cls.BitAlias.STATE_NIGHT_GRID:
                cls.is_state_night_grid(status),
            cls.BitAlias.STATE_DAY_UPS:
                cls.is_state_day_ups(status),
            cls.BitAlias.STATE_NIGHT_UPS:
                cls.is_state_night_ups(status),
            cls.BitAlias.CALIBRATION_ENABLED:
                cls.is_calibration_enabled(status),
            cls.BitAlias.CALIBRATION_IN_PROGRESS:
                cls.is_calibration_in_progress(status),
            cls.BitAlias.TURNED_ON_MANUALLY:
                cls.is_turned_on_manually(status),
            cls.BitAlias.WARNING_CURRENT_GENERAL:
                cls.is_warning_current_general(status),
            cls.BitAlias.ERROR_IO_GENERAL:
                cls.is_error_io_general(status),
            cls.BitAlias.ERROR_CURRENT_GENERAL:
                cls.is_error_current_general(status)
            }


class SHVSignalControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVSignalStatusNode(path=f'{path}/status')
        """[DWORD] Signal status."""
        self.symbol: dict[str, SHVSignalSymbolControlNode] = {}
        """Signal symbols nodes."""

    async def calibrate(self, **kwargs) -> shv.SHVType:
        """Calibrate the signal."""
        return await self.call("calibrate", **kwargs)

    async def turn_on(self, **kwargs) -> shv.SHVType:
        """
        Turn on the test of the signal
        (the calibration button has to be pressed in the control cabinet).
        """
        return await self.call("turnOn", **kwargs)

    async def turn_off(self, **kwargs) -> shv.SHVType:
        """Turn off the test of the signal."""
        return await self.call("turnOff", **kwargs)


###############################################################################
# MATRIX
###############################################################################

class SHVMatrixStatusNode(SHVStatusNode):
    class BitAlias(enum.IntEnum):
        TURNED_ON_MANUALLY = 1 << 0
        """
        Matrix test is running (can be switched off by the TEST OFF button,
        calibration deactivation, or after reaching maximum test time
        of 60 minutes).
        """
        ERROR_COMMUNICATION = 1 << 30
        """Error of communication between the PLC and the Matrix signal."""

    class BitMask(enum.IntFlag):
        TURNED_ON_MANUALLY = 1 << 0
        """
        Matrix test is running (can be switched off by the TEST OFF button,
        calibration deactivation, or after reaching maximum test time
        of 60 minutes).
        """
        ERROR_COMMUNICATION = 1 << 30
        """Error of communication between the PLC and the Matrix signal."""

    @classmethod
    def is_turned_on_manually(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.TURNED_ON_MANUALLY,
            mask=cls.BitMask.TURNED_ON_MANUALLY
            )

    @classmethod
    def is_error_communication(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_COMMUNICATION,
            mask=cls.BitMask.ERROR_COMMUNICATION
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.TURNED_ON_MANUALLY:
                cls.is_turned_on_manually(status),
            cls.BitAlias.ERROR_COMMUNICATION:
                cls.is_error_communication(status),
            }


class SHVMAtrixControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVMatrixStatusNode(path=f'{path}/status')
        """[DWORD] Matrix signal status."""
        self.data = SHVPropertySetterNode(path=f'{path}/data')
        """Matrix signal contents and configuration data."""

    async def set_test_on(self, **kwargs) -> shv.SHVType:
        """Turn on the matrix signal test mode."""
        return await self.call("setTestOn", **kwargs)

    async def set_test_off(self, **kwargs) -> shv.SHVType:
        """Turn off the matrix signal test mode."""
        return await self.call("setTestOff", **kwargs)


###############################################################################
# DOOR DISPLAY / NR LAMP
###############################################################################

class SHVDoorDisplayStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        FAILURE_DETECTED = 1 << 16
        """Signal failure detected by a TCD unit."""
        POWER_SUPPLY_MISSING = 1 << 17
        """Signal power supply missing or is not working."""

    class BitMask(enum.IntFlag):
        COLOR = 0xFF  # bits 0-7
        """Color of the display."""
        FAILURE_DETECTED = 1 << 16
        """Signal failure detected by a TCD unit"""
        POWER_SUPPLY_MISSING = 1 << 17
        """Signal power supply missing or is not working."""

    @classmethod
    def color(cls, status: int) -> int:
        return status & cls.BitMask.COLOR

    @classmethod
    def is_failure_detected(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.FAILURE_DETECTED,
            mask=cls.BitMask.FAILURE_DETECTED
            )

    @classmethod
    def is_power_supply_missing(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.POWER_SUPPLY_MISSING,
            mask=cls.BitMask.POWER_SUPPLY_MISSING
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.FAILURE_DETECTED:
                cls.is_failure_detected(status),
            cls.BitAlias.POWER_SUPPLY_MISSING:
                cls.is_power_supply_missing(status),
            }

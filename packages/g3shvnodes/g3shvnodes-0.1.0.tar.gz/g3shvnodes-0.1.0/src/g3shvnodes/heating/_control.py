import enum

import shv

from ..node._node import (
    SHVNode,
    SHVPropertyNode,
    SHVPropertySetterNode,
    SHVStatusNode,
)


###############################################################################
# HEATING CONTACTOR ROD
###############################################################################

class SHVHeatingContactorRodStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        STATE_NORMAL = 0
        """
        Rod is operating normally, current in the rod is within allowed limits.
        """
        STATE_SHORT_CIRCUIT = 1
        """
        Rod is short-circuited (for OS4P and Measured rod types, this means
        that the current in the rod is above 10% of the calibrated current
        while the rod should not be powered; for Non-Measured rod type, this
        means that the rod's digital input is active while the rod should not
        be powered).
        """
        STATE_PARTIAL_SHORT_CIRCUIT = 2
        """
        Rod is partially short-circuited (only for OS4P and Measured rod types;
        the current in the rod is above 130% of the calibrated current).
        """
        STATE_BREAK = 3
        """
        Rod is broken (for OS4P and Measured rod types, this means that the
        current in the rod is below 50% of calibrated current; for Non-Measured
        rod type, this means that the rod's digital input is inactive when the
        rod should be powered). Alternatively, the rod is missing.
        """
        STATE_PARTIAL_BREAK = 4
        """
        Rod is partially broken (only for OS4P and Measured rod types;
        the current in the rod is below 70% of the calibrated current).
        """
        HEATING_ON = 1 << 8
        """
        Heating rod is switched on by a switch heating unit and is heating.
        """
        CALIBRATED = 1 << 9
        """
        Heating rod is calibrated at its nominal current.
        """
        WARNING_GENERAL = 1 << 25
        """
        General warning (due to a partial break or a partial short-circuit).
        """
        ERROR_GENERAL = 1 << 26
        """
        General error (due to a break or a short-circuit).
        """

    class BitMask(enum.IntFlag):
        STATE = 0b111
        """
        Heating rod state.
        """
        HEATING_ON = 1 << 8
        """
        Heating rod is switched on by a switch heating unit and is heating.
        """
        CALIBRATED = 1 << 9
        """
        Heating rod is calibrated at its nominal current.
        """
        WARNING_GENERAL = 1 << 25
        """
        General warning (due to a partial break or a partial short-circuit).
        """
        ERROR_GENERAL = 1 << 26
        """
        General error (due to a break or a short-circuit).
        """

    @classmethod
    def is_state_normal(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_NORMAL,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_short_circuit(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_SHORT_CIRCUIT,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_partial_short_circuit(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_PARTIAL_SHORT_CIRCUIT,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_break(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_BREAK,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_partial_break(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_PARTIAL_BREAK,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_heating_on(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.HEATING_ON,
            mask=cls.BitMask.HEATING_ON
            )

    @classmethod
    def is_calibrated(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.CALIBRATED,
            mask=cls.BitMask.CALIBRATED
            )

    @classmethod
    def is_warning_general(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.WARNING_GENERAL,
            mask=cls.BitMask.WARNING_GENERAL
            )

    @classmethod
    def is_error_general(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_GENERAL,
            mask=cls.BitMask.ERROR_GENERAL
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.STATE_NORMAL:
                cls.is_state_normal(status),
            cls.BitAlias.STATE_SHORT_CIRCUIT:
                cls.is_state_short_circuit(status),
            cls.BitAlias.STATE_PARTIAL_SHORT_CIRCUIT:
                cls.is_state_partial_short_circuit(status),
            cls.BitAlias.STATE_BREAK:
                cls.is_state_break(status),
            cls.BitAlias.STATE_PARTIAL_BREAK:
                cls.is_state_partial_break(status),
            cls.BitAlias.HEATING_ON:
                cls.is_heating_on(status),
            cls.BitAlias.CALIBRATED:
                cls.is_calibrated(status),
            cls.BitAlias.WARNING_GENERAL:
                cls.is_warning_general(status),
            cls.BitAlias.ERROR_GENERAL:
                cls.is_error_general(status)
            }


class SHVHeatingContactorRodControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVHeatingContactorRodStatusNode(
            path=f'{path}/status'
            )
        """[DWORD] Heating rod status."""
        self.calibrated_current = SHVPropertyNode(
            path=f'{path}/calibratedCurrent'
            )
        """[REAL, A] Calibrated heating rod current."""


###############################################################################
# HEATING CONTACTOR
###############################################################################

class SHVHeatingContactorStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        CONTACTOR_ON = 1 << 0
        """
        Heating contactor (switch heating unit) is switched on.
        """
        CALIBRATION = 1 << 5
        """
        Heating contactor's (Switch heating unit's) heating rods are being
        calibrated.
        """
        MODULE_OVERHEATING = 1 << 28
        """
        Heating contactor (switch heating unit) is overheating
        (cooling of the unit is not sufficient). Only for OS4P type switch
        heating units.
        """
        ERROR_OS4P_MODULE = 1 << 29
        """
        Error of the heating contactor (switch heating unit) detected.
        Only for OS4P type switch heating units.
        """
        ERROR_COMMUNICATION = 1 << 30
        """
        Communication error of the heating contactor (switch heating unit)
        detected. Only for OS4P type switch heating units.
        """

    class BitMask(enum.IntFlag):
        CONTACTOR_ON = 1 << 0
        """
        Heating contactor (switch heating unit) is switched on.
        """
        CALIBRATION = 1 << 5
        """
        Heating contactor's (Switch heating unit's) heating rods are being
        calibrated.
        """
        MODULE_OVERHEATING = 1 << 28
        """
        Heating contactor (switch heating unit) is overheating
        (cooling of the unit is not sufficient). Only for OS4P type switch
        heating units.
        """
        ERROR_OS4P_MODULE = 1 << 29
        """
        Error of the heating contactor (switch heating unit) detected.
        Only for OS4P type switch heating units.
        """
        ERROR_COMMUNICATION = 1 << 30
        """
        Communication error of the heating contactor (switch heating unit)
        detected. Only for OS4P type switch heating units.
        """

    @classmethod
    def is_contactor_on(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.CONTACTOR_ON,
            mask=cls.BitMask.CONTACTOR_ON
            )

    @classmethod
    def is_calibration(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.CALIBRATION,
            mask=cls.BitMask.CALIBRATION
            )

    @classmethod
    def is_module_overheating(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.MODULE_OVERHEATING,
            mask=cls.BitMask.MODULE_OVERHEATING
            )

    @classmethod
    def is_error_os4p_module(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_OS4P_MODULE,
            mask=cls.BitMask.ERROR_OS4P_MODULE
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
            cls.BitAlias.CONTACTOR_ON:
                cls.is_contactor_on(status),
            cls.BitAlias.CALIBRATION:
                cls.is_calibration(status),
            cls.BitAlias.MODULE_OVERHEATING:
                cls.is_module_overheating(status),
            cls.BitAlias.ERROR_OS4P_MODULE:
                cls.is_error_os4p_module(status),
            cls.BitAlias.ERROR_COMMUNICATION:
                cls.is_error_communication(status)
            }


class SHVHeatingContactorControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVHeatingContactorStatusNode(path=f'{path}/status')
        """[DWORD] Heating contactor status."""
        self.heating_power = SHVPropertyNode(path=f'{path}/heatingPower')
        """[INT, %] Calculated heating power sent to the heating contactor."""
        self.rod: dict[str, SHVHeatingContactorRodControlNode] = {}
        """Heating contactor rods control nodes."""

    async def calibrate(self) -> shv.SHVType:
        """
        Start calibration of all heating rods connected to the heating
        contactor (switch heating unit).
        """
        return await self.call('calibrate')


###############################################################################
# HEATING
###############################################################################

class SHVHeatingStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        STATE_OFF = 0 << 0
        """
        Heating is switched OFF, desired heating power is 0%.
        """
        STATE_ON_PERMANENT = 1 << 0
        """
        Heating is switched ON to full power, desired heating power is 100%.
        """
        STATE_AUTO = 2 << 0
        """
        Heating is is the automatic mode. It operates based on the temperature
        inputs and precipitation sensor binary input.
        """
        TEST = 1 << 3
        """
        Heating is in test mode.
        """
        HEATING_ACTIVATED_MANUALLY = 1 << 4
        """
        Heating was manually activated.
        """
        WET_CONDITIONS = 1 << 8
        """
        Wet conditions are detected.
        """
        CONTACTOR_SWITCHED_ON = 1 << 16
        """
        The contactor for the heating is switched on.
        """
        METEO_HEATING = 1 << 17
        """
        The meteo heating is active.
        """
        NOTICE_LOW_TEMP_RAIL_SETPOINT = 1 << 18
        """
        The rail temperature is below the setpoint.
        """
        NOTICE_LOW_TEMP_RAIL_MINIMUM = 1 << 19
        """
        The rail temperature is below the minimum.
        """
        NOTICE_LOW_TEMP_AIR_ZERO_POWER = 1 << 20
        """
        The air temperature is low enough to turn off the heating.
        """
        WARNING_DISABLED_FROM_CABINET = 1 << 23
        """
        The heating was disabled from the cabinet.
        """
        ERROR_METEO_GENERAL = 1 << 24
        """
        There is a general error with the meteo heating.
        """
        ERROR_METEO_SENSOR = 1 << 25
        """
        There is an error with the meteo sensor.
        """
        ERROR_METEO_HEATING = 1 << 26
        """
        There is an error with the meteo heating.
        """
        ERROR_TEMP_AIR = 1 << 27
        """
        There is an error with the air temperature sensor.
        """
        ERROR_TEMP_RAIL = 1 << 28
        """
        There is an error with the rail temperature sensor.
        """
        ERROR_TEMP_METEO = 1 << 29
        """
        There is an error with the meteo temperature sensor.
        """
        ERROR_AUTOMATIC_CONTROL = 1 << 30
        """
        There is an error with the automatic control of the heating.
        """

    class BitMask(enum.IntFlag):
        STATE = 0b11  # bit 0 and 1
        """
        The current state of the heating.
        """
        TEST = 1 << 3
        """
        Heating is in test mode.
        """
        HEATING_ACTIVATED_MANUALLY = 1 << 4
        """
        Heating was manually activated.
        """
        WET_CONDITIONS = 1 << 8
        """
        Wet conditions are detected.
        """
        CONTACTOR_SWITCHED_ON = 1 << 16
        """
        The contactor for the heating is switched on.
        """
        METEO_HEATING = 1 << 17
        """
        The meteo heating is active.
        """
        NOTICE_LOW_TEMP_RAIL_SETPOINT = 1 << 18
        """
        The rail temperature is below the setpoint.
        """
        NOTICE_LOW_TEMP_RAIL_MINIMUM = 1 << 19
        """
        The rail temperature is below the minimum.
        """
        NOTICE_LOW_TEMP_AIR_ZERO_POWER = 1 << 20
        """
        The air temperature is low enough to turn off the heating.
        """
        WARNING_DISABLED_FROM_CABINET = 1 << 23
        """
        The heating was disabled from the cabinet.
        """
        ERROR_METEO_GENERAL = 1 << 24
        """
        There is a general error with the meteo heating.
        """
        ERROR_METEO_SENSOR = 1 << 25
        """
        There is an error with the meteo sensor.
        """
        ERROR_METEO_HEATING = 1 << 26
        """
        There is an error with the meteo heating.
        """
        ERROR_TEMP_AIR = 1 << 27
        """
        There is an error with the air temperature sensor.
        """
        ERROR_TEMP_RAIL = 1 << 28
        """
        There is an error with the rail temperature sensor.
        """
        ERROR_TEMP_METEO = 1 << 29
        """
        There is an error with the meteo temperature sensor.
        """
        ERROR_AUTOMATIC_CONTROL = 1 << 30
        """
        There is an error with the automatic control of the heating.
        """

    @classmethod
    def is_state_off(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_OFF,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_on_permanent(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_ON_PERMANENT,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_auto(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_AUTO,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_test(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.TEST,
            mask=cls.BitMask.TEST
            )

    @classmethod
    def is_heating_activated_manually(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.HEATING_ACTIVATED_MANUALLY,
            mask=cls.BitMask.HEATING_ACTIVATED_MANUALLY
            )

    @classmethod
    def is_wet_conditions(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.WET_CONDITIONS,
            mask=cls.BitMask.WET_CONDITIONS
            )

    @classmethod
    def is_contactor_switched_on(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.CONTACTOR_SWITCHED_ON,
            mask=cls.BitMask.CONTACTOR_SWITCHED_ON
            )

    @classmethod
    def is_meteo_heating(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.METEO_HEATING,
            mask=cls.BitMask.METEO_HEATING
            )

    @classmethod
    def is_notice_low_temp_rail_setpoint(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.NOTICE_LOW_TEMP_RAIL_SETPOINT,
            mask=cls.BitMask.NOTICE_LOW_TEMP_RAIL_SETPOINT
            )

    @classmethod
    def is_notice_low_temp_rail_minimum(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.NOTICE_LOW_TEMP_RAIL_MINIMUM,
            mask=cls.BitMask.NOTICE_LOW_TEMP_RAIL_MINIMUM
            )

    @classmethod
    def is_notice_low_temp_air_zero_power(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.NOTICE_LOW_TEMP_AIR_ZERO_POWER,
            mask=cls.BitMask.NOTICE_LOW_TEMP_AIR_ZERO_POWER
            )

    @classmethod
    def is_warning_disabled_from_cabinet(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.WARNING_DISABLED_FROM_CABINET,
            mask=cls.BitMask.WARNING_DISABLED_FROM_CABINET
            )

    @classmethod
    def is_error_meteo_general(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_METEO_GENERAL,
            mask=cls.BitMask.ERROR_METEO_GENERAL
            )

    @classmethod
    def is_error_meteo_sensor(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_METEO_SENSOR,
            mask=cls.BitMask.ERROR_METEO_SENSOR
            )

    @classmethod
    def is_error_meteo_heating(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_METEO_HEATING,
            mask=cls.BitMask.ERROR_METEO_HEATING
            )

    @classmethod
    def is_error_temp_air(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_TEMP_AIR,
            mask=cls.BitMask.ERROR_TEMP_AIR
            )

    @classmethod
    def is_error_temp_rail(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_TEMP_RAIL,
            mask=cls.BitMask.ERROR_TEMP_RAIL
            )

    @classmethod
    def is_error_temp_meteo(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_TEMP_METEO,
            mask=cls.BitMask.ERROR_TEMP_METEO
            )

    @classmethod
    def is_error_automatic_control(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_AUTOMATIC_CONTROL,
            mask=cls.BitMask.ERROR_AUTOMATIC_CONTROL
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.STATE_OFF:
                cls.is_state_off(status),
            cls.BitAlias.STATE_ON_PERMANENT:
                cls.is_state_on_permanent(status),
            cls.BitAlias.STATE_AUTO:
                cls.is_state_auto(status),
            cls.BitAlias.TEST:
                cls.is_test(status),
            cls.BitAlias.HEATING_ACTIVATED_MANUALLY:
                cls.is_heating_activated_manually(status),
            cls.BitAlias.WET_CONDITIONS:
                cls.is_wet_conditions(status),
            cls.BitAlias.CONTACTOR_SWITCHED_ON:
                cls.is_contactor_switched_on(status),
            cls.BitAlias.METEO_HEATING:
                cls.is_meteo_heating(status),
            cls.BitAlias.NOTICE_LOW_TEMP_RAIL_SETPOINT:
                cls.is_notice_low_temp_rail_setpoint(status),
            cls.BitAlias.NOTICE_LOW_TEMP_RAIL_MINIMUM:
                cls.is_notice_low_temp_rail_minimum(status),
            cls.BitAlias.NOTICE_LOW_TEMP_AIR_ZERO_POWER:
                cls.is_notice_low_temp_air_zero_power(status),
            cls.BitAlias.WARNING_DISABLED_FROM_CABINET:
                cls.is_warning_disabled_from_cabinet(status),
            cls.BitAlias.ERROR_METEO_GENERAL:
                cls.is_error_meteo_general(status),
            cls.BitAlias.ERROR_METEO_SENSOR:
                cls.is_error_meteo_sensor(status),
            cls.BitAlias.ERROR_METEO_HEATING:
                cls.is_error_meteo_heating(status),
            cls.BitAlias.ERROR_TEMP_AIR:
                cls.is_error_temp_air(status),
            cls.BitAlias.ERROR_TEMP_RAIL:
                cls.is_error_temp_rail(status),
            cls.BitAlias.ERROR_TEMP_METEO:
                cls.is_error_temp_meteo(status),
            cls.BitAlias.ERROR_AUTOMATIC_CONTROL:
                cls.is_error_automatic_control(status),
            }


class SHVHeatingConfigNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.temp_air_zero_power = SHVPropertySetterNode(
            path=f'{path}/tempAirZeroPower'
            )
        """
        [INT, °C] Maximum air temperature for the automatic controller.
        Heating is switched off above this limit.
        """
        self.temp_rail_setpoint = SHVPropertySetterNode(
            path=f'{path}/tempRailSetpoint'
            )
        """
        [INT, °C] Desired rail temperature for automatic control
        (from zero for wet conditions, from dew point for dry conditions).
        """
        self.temp_rail_hysteresis = SHVPropertySetterNode(
            path=f'{path}/tempRailHysteresis'
            )
        """
        [INT, °C] Bandwidth below the target temperature
        for switching on the heating.
        """
        self.temp_rail_minimum = SHVPropertySetterNode(
            path=f'{path}/tempRailMinimum'
            )
        """
        [INT, °C] Minimum rail temperature for dry conditions.
        """
        self.temp_difference_dry = SHVPropertySetterNode(
            path=f'{path}/tempDifferenceDry'
            )
        """
        [INT, °C] For dry conditions, the minimum difference between
        the desired rail temperature and the air temperature. Below this
        threshold, the heating power output increases linearly from 0% to 100%.
        If this temperature difference is exceeded, the heating power remains
        consistently at 100%.
        """
        self.temp_difference_wet = SHVPropertySetterNode(
            path=f'{path}/tempDifferenceWet'
            )
        """
        [INT, °C] For wet conditions, the minimum difference between
        the desired rail temperature and the air temperature. Below this
        threshold, the heating power output increases linearly from 0% to 100%.
        If this temperature difference is exceeded, the heating power remains
        consistently at 100%.
        """
        self.test_time = SHVPropertySetterNode(
            path=f'{path}/testTime'
            )
        """[INT, min] Maximum duration of a heating test."""


class SHVHeatingControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVHeatingStatusNode(path=f'{path}/status')
        """[DWORD] Heating status."""
        self.config = SHVHeatingConfigNode(path=f'{path}/config')
        """Heating configuration."""
        self.temp_air = SHVPropertyNode(path=f'{path}/tempAir')
        """[REAL, °C] Measured ambient air temperature."""
        self.temp_rail = SHVPropertyNode(path=f'{path}/tempRail')
        """[REAL, °C] Measured rail temperature."""
        self.temp_meteo = SHVPropertyNode(path=f'{path}/tempMeteo')
        """[REAL, °C] Measured temperature of meteo unit."""
        self.contactor: dict[str, SHVHeatingContactorControlNode] = {}
        """Heating contactors control nodes."""

    async def set_auto(self, **kwargs) -> shv.SHVType:
        """Activate automatic mode of heating control logic."""
        return await self.call('setAuto', **kwargs)

    async def set_off(self, **kwargs) -> shv.SHVType:
        """Deactivate permanent heating."""
        return await self.call('setOff', **kwargs)

    async def set_on(self, **kwargs) -> shv.SHVType:
        """Activate permanent heating."""
        return await self.call('setOn', **kwargs)

    async def set_test_on(self, **kwargs) -> shv.SHVType:
        """Switch the heating test ON."""
        return await self.call('setTestOn', **kwargs)

    async def set_test_off(self, **kwargs) -> shv.SHVType:
        """Switch the heating test OFF."""
        return await self.call('setTestOff', **kwargs)

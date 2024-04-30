import enum

import shv

from ..node._node import (
    SHVNode,
    SHVPropertyNode,
    SHVPropertySetterNode,
    SHVStatusNode,
)


###############################################################################
# CABINET - UPS
###############################################################################

class SHVCabinetUPSStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        UPS_READY = 1 << 0
        """
        UPS unit is connected and ready.
        """
        UPS_BUFFERING = 1 << 1
        """
        UPS battery is connected and is powering the system.
        """
        REPLACE_BATTERY_WARNING = 1 << 2
        """
        UPS battery needs to be replaced.
        """
        WARNING_POWERED_FROM_UPS = 1 << 17
        """
        UPS is currently powering the cabinet from battery
        (UPS mode evaluated by the control PLC).
        """

    class BitMask(enum.IntFlag):
        UPS_READY = 1 << 0
        """
        UPS unit is connected and ready.
        """
        UPS_BUFFERING = 1 << 1
        """
        UPS battery is connected and is powering the system.
        """
        REPLACE_BATTERY_WARNING = 1 << 2
        """
        UPS battery needs to be replaced.
        """
        WARNING_POWERED_FROM_UPS = 1 << 17
        """
        UPS is currently powering the cabinet from battery
        (UPS mode evaluated by the control PLC).
        """

    @classmethod
    def is_ups_ready(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.UPS_READY,
            mask=cls.BitMask.UPS_READY
            )

    @classmethod
    def is_ups_buffering(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.UPS_BUFFERING,
            mask=cls.BitMask.UPS_BUFFERING
            )

    @classmethod
    def is_replace_battery_warning(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.REPLACE_BATTERY_WARNING,
            mask=cls.BitMask.REPLACE_BATTERY_WARNING
            )

    @classmethod
    def is_warning_powered_from_ups(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.WARNING_POWERED_FROM_UPS,
            mask=cls.BitMask.WARNING_POWERED_FROM_UPS
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.UPS_READY:
                cls.is_ups_ready(status),
            cls.BitAlias.UPS_BUFFERING:
                cls.is_ups_buffering(status),
            cls.BitAlias.REPLACE_BATTERY_WARNING:
                cls.is_replace_battery_warning(status),
            cls.BitAlias.WARNING_POWERED_FROM_UPS:
                cls.is_warning_powered_from_ups(status)
            }


class SHVCabineUPSConfigNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.degradation_time = SHVPropertySetterNode(
            path=f'{path}/degradationTime'
            )
        """
        [INT, s] Delay in seconds to set the zone to the AB or the EI state
        when the cabinet is powered from UPS.
        """


class SHVCabineUPSNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVCabinetUPSStatusNode(path=f'{path}/status')
        """[DWORD] Cabine UPS status."""
        self.config = SHVCabineUPSConfigNode(path=f'{path}/config')
        """Cabine UPS configuration."""


###############################################################################
# CABINET - FUSE
###############################################################################

class SHVCabinetFuseStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        ERROR_FUSE_BREAK = 1 << 30
        """Fuse is broken or disconnected."""

    class BitMask(enum.IntFlag):
        ERROR_FUSE_BREAK = 1 << 30
        """Fuse is broken or disconnected."""

    @classmethod
    def is_error_fuse_break(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_FUSE_BREAK,
            mask=cls.BitMask.ERROR_FUSE_BREAK
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.ERROR_FUSE_BREAK: cls.is_error_fuse_break(status)
            }


class SHVCabinetFuseNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVCabinetFuseStatusNode(path=f'{path}/status')
        """[DWORD] Cabine fuse status."""


###############################################################################
# CABINET - CONVERTOR
###############################################################################

class SHVCabinetConvertorStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        CONVERTOR_INACTIVE = 1 << 0
        """
        Convertor power supply is not active
        (e.g. due to error, disconnected, etc.).
        """

    class BitMask(enum.IntFlag):
        CONVERTOR_INACTIVE = 1 << 0
        """
        Convertor power supply is not active
        (e.g. due to error, disconnected, etc.).
        """

    @classmethod
    def is_convertor_inactive(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.CONVERTOR_INACTIVE,
            mask=cls.BitMask.CONVERTOR_INACTIVE
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.CONVERTOR_INACTIVE: cls.is_convertor_inactive(status)
            }


class SHVCabinetConvertorNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVCabinetConvertorStatusNode(path=f'{path}/status')
        """[DWORD] Cabine convertor status."""


###############################################################################
# CABINET - RFID
###############################################################################

class SHVCabinetRFIDStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        USER_LOGGED_IN = 1 << 0
        """User RFID tag number has been recorded."""
        WARNING_ALARM = 1 << 1
        """User RFID tag has not bben identified. Alarm is active."""

    class BitMask(enum.IntFlag):
        USER_LOGGED_IN = 1 << 0
        """User RFID tag number has been recorded."""
        WARNING_ALARM = 1 << 1
        """User RFID tag has not bben identified. Alarm is active."""

    @classmethod
    def is_user_logged_in(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.USER_LOGGED_IN,
            mask=cls.BitMask.USER_LOGGED_IN
            )

    @classmethod
    def is_warning_alarm(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.WARNING_ALARM,
            mask=cls.BitMask.WARNING_ALARM
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.USER_LOGGED_IN: cls.is_user_logged_in(status),
            cls.BitAlias.WARNING_ALARM: cls.is_warning_alarm(status)
            }


class SHVCabinetRFIDNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVCabinetRFIDStatusNode(path=f'{path}/status')
        """[DWORD] Cabine RFID status."""
        self.user_id = SHVPropertyNode(path=f'{path}/userID')
        """[STRING] Last user RFID tag number recorded."""


###############################################################################
# CABINET - MONITORING MODULE
###############################################################################

class SHVCabinetMonitoringModuleNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.humidity = SHVPropertySetterNode(
            path=f'{path}/humidity'
            )
        """
        [INT, %] Humidity inside the cabinet measured by the monitoring module.
        """
        self.temperature = SHVPropertySetterNode(
            path=f'{path}/temperature'
            )
        """
        [REAL, °C] Temperature inside the cabinet measured
        by the monitoring module.
        """
        self.power_on_cycles = SHVPropertySetterNode(
            path=f'{path}/powerOnCycles'
            )
        """
        [UDINT] Number of power-on cycles
        (how many times the cabinet has been powered on).
        """
        self.operation_time = SHVPropertySetterNode(
            path=f'{path}/operationTime'
            )
        """[UDINT, hours] Total operating time of the monitoring module."""
        self.acceleration01_min = SHVPropertySetterNode(
            path=f'{path}/acceleration01Min'
            )
        """[INT, N⋅m2/kg2] Minimum acceleration value (direction 01)."""
        self.acceleration01_max = SHVPropertySetterNode(
            path=f'{path}/acceleration01Max'
            )
        """[INT, N⋅m2/kg2] Maximum acceleration value (direction 01)."""
        self.acceleration02_min = SHVPropertySetterNode(
            path=f'{path}/acceleration02Min'
            )
        """[INT, N⋅m2/kg2] Minimum acceleration value (direction 02)."""
        self.acceleration02_max = SHVPropertySetterNode(
            path=f'{path}/acceleration02Max'
            )
        """[INT, N⋅m2/kg2] Maximum acceleration value (direction 02)."""
        self.acceleration03_min = SHVPropertySetterNode(
            path=f'{path}/acceleration03Min'
            )
        """[INT, N⋅m2/kg2] Minimum acceleration value (direction 03)."""
        self.acceleration03_max = SHVPropertySetterNode(
            path=f'{path}/acceleration03Max'
            )
        """[INT, N⋅m2/kg2] Maximum acceleration value (direction 03)."""

    async def clear_values(self, **kwargs) -> shv.SHVType:
        """Clear all saved values except humidity and temperature."""
        return await self.call('clearValues', **kwargs)


###############################################################################
# CABINET - SMS
###############################################################################

class SHVCabinetSMSStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        WAITING = 1 << 0
        """
        Waiting. SMS function is running and is waiting for any SMS to send.
        """
        SENDING = 1 << 1
        """
        Sending. The SMS is currently being sent.
        """
        TCP_CLIENT_ERROR = 1 << 10
        """
        TCP client error. SMS function is not connected to a GSM modem.
        """
        GSM_MODE_ERROR = 1 << 11
        """
        GSM mode error. SMS mode cannot be set in the GSM modem.
        """
        NETWORK_DISCONNECTED = 1 << 12
        """
        Network disconnected.
        GSM modem is not connected to the cellular network.
        """

    class BitMask(enum.IntFlag):
        STATE = 0xFF  # bits 0-7
        """
        Cabinet SMS state.
        """

    @classmethod
    def is_waiting(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.WAITING,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_sending(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.SENDING,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_tcp_client_error(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.TCP_CLIENT_ERROR,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_gsm_mode_error(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.GSM_MODE_ERROR,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_network_disconnected(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.NETWORK_DISCONNECTED,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.WAITING:
                cls.is_waiting(status),
            cls.BitAlias.SENDING:
                cls.is_sending(status),
            cls.BitAlias.TCP_CLIENT_ERROR:
                cls.is_tcp_client_error(status),
            cls.BitAlias.GSM_MODE_ERROR:
                cls.is_gsm_mode_error(status),
            cls.BitAlias.NETWORK_DISCONNECTED:
                cls.is_network_disconnected(status)
            }


class SHVCabinetSMSNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVCabinetSMSStatusNode(
            path=f'{path}/status'
            )
        """[DWORD] Cabine SMS status."""
        self.counter_sent_sms = SHVPropertyNode(
            path=f'{path}/counterSentSMS'
            )
        """[UINT] Counter of all SMS sent."""
        self.counter_sent_sms_per_hour = SHVPropertyNode(
            path=f'{path}/counterSentSMSPerHour'
            )
        """[UINT] Counter of SMS sent during the last hour."""
        self.counter_failed_sms = SHVPropertyNode(
            path=f'{path}/counterFailedSMS'
            )
        """
        [UINT] Counter of all failed SMS
        (due to a network error, a send error, etc.).
        """
        self.phone_numbers = SHVPropertyNode(
            path=f'{path}/phoneNumbers'
            )
        """[STRING] Predefined phone numbers to send SMS to."""

    async def reboot(self, **kwargs) -> shv.SHVType:
        """Reset connection to the GSM modem (reinitialize SMS function)."""
        return await self.call('reboot', **kwargs)

    async def reset_counters(self, **kwargs) -> shv.SHVType:
        """Reset all SMS counters."""
        return await self.call('resetCounters', **kwargs)


###############################################################################
# CABINET
###############################################################################

class SHVCabinetStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        CALIBRATION_ENABLED = 1 << 0
        """
        Signal calibration procedure is enabled by pressing the button
        in cabinet.
        """
        ACTIVE_TWILIGHT_SENSOR = 1 << 1
        """
        Luminance sensor (YES = Night, NO = Day).
        """
        ACTIVE_FAN = 1 << 2
        """
        Internal cabinet fan is active.
        """
        VOLTAGE_CATENARY_NOT_PRESENT = 1 << 3
        """
        Catenary voltage is not present.
        """
        VOLTAGE_230V_NOT_PRESENT = 1 << 4
        """
        230VAC power supply is not present.
        """
        ERROR_MAIN_SWITCH = 1 << 5
        """
        Main switch auxillary contact is open.
        """
        WARNING_DOOR_OPENED = 1 << 17
        """
        Cabinet door is currently open.
        """
        COMPONENT_WARNING = 1 << 22
        """
        Any warning caused by a component in the cabinet (e.g. UPS).
        Used only to display an alarm on visualization.
        """
        COMPONENT_ERROR = 1 << 23
        """
        Any error caused by a component in the cabinet (e.g. UPS).
        Used only to display an alarm on visualization.
        """
        ERROR_VOLTAGE_600V = 1 << 24
        """
        Catenary (OCL) voltage is out of limits (+/- 5%) or measurement error.
        """
        ERROR_VOLTAGE_24V = 1 << 25
        """
        Voltage at the 24V bus is out of limits (+/- 5%) or measurement error.
        """
        ERROR_OVER_TEMPERATURE = 1 << 26
        """
        Upper or bottom temperature is out of limits or measurement error.
        """
        ERROR_NORM_BUTTON = 1 << 27
        """
        Complementarity error or
        hardware input error of the NORM hardware button.
        """
        ERROR_AB_BUTTON = 1 << 28
        """
        Complementarity error or
        hardware input error of the AB hardware button.
        """
        ERROR_EI_BUTTON = 1 << 29
        """
        Complementarity error or
        hardware input error of the EI hardware button.
        """
        ERROR_CALIBRATION_BUTTON = 1 << 30
        """
        Complementarity error or
        hardware input error of the calibration hardware button.
        """

    class BitMask(enum.IntFlag):
        CALIBRATION_ENABLED = 1 << 0
        """
        Signal calibration procedure is enabled by pressing the button
        in cabinet.
        """
        ACTIVE_TWILIGHT_SENSOR = 1 << 1
        """
        Luminance sensor (YES = Night, NO = Day).
        """
        ACTIVE_FAN = 1 << 2
        """
        Internal cabinet fan is active.
        """
        VOLTAGE_CATENARY_NOT_PRESENT = 1 << 3
        """
        Catenary voltage is not present.
        """
        VOLTAGE_230V_NOT_PRESENT = 1 << 4
        """
        230VAC power supply is not present.
        """
        ERROR_MAIN_SWITCH = 1 << 5
        """
        Main switch auxillary contact is open.
        """
        WARNING_DOOR_OPENED = 1 << 17
        """
        Cabinet door is currently open.
        """
        COMPONENT_WARNING = 1 << 22
        """
        Any warning caused by a component in the cabinet (e.g. UPS).
        Used only to display an alarm on visualization.
        """
        COMPONENT_ERROR = 1 << 23
        """
        Any error caused by a component in the cabinet (e.g. UPS).
        Used only to display an alarm on visualization.
        """
        ERROR_VOLTAGE_600V = 1 << 24
        """
        Catenary (OCL) voltage is out of limits (+/- 5%) or measurement error.
        """
        ERROR_VOLTAGE_24V = 1 << 25
        """
        Voltage at the 24V bus is out of limits (+/- 5%) or measurement error.
        """
        ERROR_OVER_TEMPERATURE = 1 << 26
        """
        Upper or bottom temperature is out of limits or measurement error.
        """
        ERROR_NORM_BUTTON = 1 << 27
        """
        Complementarity error or
        hardware input error of the NORM hardware button.
        """
        ERROR_AB_BUTTON = 1 << 28
        """
        Complementarity error or
        hardware input error of the AB hardware button.
        """
        ERROR_EI_BUTTON = 1 << 29
        """
        Complementarity error or
        hardware input error of the EI hardware button.
        """
        ERROR_CALIBRATION_BUTTON = 1 << 30
        """
        Complementarity error or
        hardware input error of the calibration hardware button.
        """

    @classmethod
    def is_calibration_enabled(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.CALIBRATION_ENABLED,
            mask=cls.BitMask.CALIBRATION_ENABLED
            )

    @classmethod
    def is_active_twilight_sensor(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ACTIVE_TWILIGHT_SENSOR,
            mask=cls.BitMask.ACTIVE_TWILIGHT_SENSOR
            )

    @classmethod
    def is_active_fan(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ACTIVE_FAN,
            mask=cls.BitMask.ACTIVE_FAN
            )

    @classmethod
    def is_voltage_catenary_not_present(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.VOLTAGE_CATENARY_NOT_PRESENT,
            mask=cls.BitMask.VOLTAGE_CATENARY_NOT_PRESENT
            )

    @classmethod
    def is_voltage_230v_not_present(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.VOLTAGE_230V_NOT_PRESENT,
            mask=cls.BitMask.VOLTAGE_230V_NOT_PRESENT
            )

    @classmethod
    def is_warning_door_opened(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.WARNING_DOOR_OPENED,
            mask=cls.BitMask.WARNING_DOOR_OPENED
            )

    @classmethod
    def is_component_warning(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.COMPONENT_WARNING,
            mask=cls.BitMask.COMPONENT_WARNING
            )

    @classmethod
    def is_component_error(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.COMPONENT_ERROR,
            mask=cls.BitMask.COMPONENT_ERROR
            )

    @classmethod
    def is_error_voltage_600V(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_VOLTAGE_600V,
            mask=cls.BitMask.ERROR_VOLTAGE_600V
            )

    @classmethod
    def is_error_voltage_24V(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_VOLTAGE_24V,
            mask=cls.BitMask.ERROR_VOLTAGE_24V
            )

    @classmethod
    def is_error_over_temperature(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_OVER_TEMPERATURE,
            mask=cls.BitMask.ERROR_OVER_TEMPERATURE
            )

    @classmethod
    def is_error_norm_button(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_NORM_BUTTON,
            mask=cls.BitMask.ERROR_NORM_BUTTON
            )

    @classmethod
    def is_error_ab_button(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_AB_BUTTON,
            mask=cls.BitMask.ERROR_AB_BUTTON
            )

    @classmethod
    def is_error_ei_button(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_EI_BUTTON,
            mask=cls.BitMask.ERROR_EI_BUTTON
            )

    @classmethod
    def is_error_calibration_button(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_CALIBRATION_BUTTON,
            mask=cls.BitMask.ERROR_CALIBRATION_BUTTON
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.CALIBRATION_ENABLED:
                cls.is_calibration_enabled(status),
            cls.BitAlias.ACTIVE_TWILIGHT_SENSOR:
                cls.is_active_twilight_sensor(status),
            cls.BitAlias.ACTIVE_FAN:
                cls.is_active_fan(status),
            cls.BitAlias.VOLTAGE_CATENARY_NOT_PRESENT:
                cls.is_voltage_catenary_not_present(status),
            cls.BitAlias.VOLTAGE_230V_NOT_PRESENT:
                cls.is_voltage_230v_not_present(status),
            cls.BitAlias.WARNING_DOOR_OPENED:
                cls.is_warning_door_opened(status),
            cls.BitAlias.COMPONENT_WARNING:
                cls.is_component_warning(status),
            cls.BitAlias.COMPONENT_ERROR:
                cls.is_component_error(status),
            cls.BitAlias.ERROR_VOLTAGE_600V:
                cls.is_error_voltage_600V(status),
            cls.BitAlias.ERROR_VOLTAGE_24V:
                cls.is_error_voltage_24V(status),
            cls.BitAlias.ERROR_OVER_TEMPERATURE:
                cls.is_error_over_temperature(status),
            cls.BitAlias.ERROR_NORM_BUTTON:
                cls.is_error_norm_button(status),
            cls.BitAlias.ERROR_AB_BUTTON:
                cls.is_error_ab_button(status),
            cls.BitAlias.ERROR_EI_BUTTON:
                cls.is_error_ei_button(status),
            cls.BitAlias.ERROR_CALIBRATION_BUTTON:
                cls.is_error_calibration_button(status)
            }


class SHVCabinetControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVCabinetStatusNode(
            path=f'{path}/status',
            )
        """[DWORD] Cabine status."""
        self.voltage600_v = SHVPropertySetterNode(
            path=f'{path}/voltage600V',
            )
        """[INT, V] Catenary voltage."""
        self.voltage24_v = SHVPropertySetterNode(
            path=f'{path}/voltage24V',
            )
        """[REAL, V] Voltage at the 24V bus."""
        self.temperature = SHVPropertySetterNode(
            path=f'{path}/temperature',
            )
        """[REAL, °C] Temperature in the upper part of the cabinet."""
        self.temperature_bottom = SHVPropertySetterNode(
            path=f'{path}/temperatureBottom',
            )
        """[REAL, °C] Temperature in the bottom part of the cabinet."""
        self.ups: dict[str, SHVCabineUPSNode] = {}
        """Cabinet UPS nodes."""
        self.fuse: dict[str, SHVCabinetFuseNode] = {}
        """Cabinet fuse nodes."""
        self.convertor: dict[str, SHVCabinetConvertorNode] = {}
        """Cabinet convertor nodes."""
        self.rfid: dict[str, SHVCabinetRFIDNode] = {}
        """Cabinet RFID nodes."""
        self.sms: dict[str, SHVCabinetSMSNode] = {}
        """Cabinet SMS nodes."""
        self.monitoring_module: dict[str, SHVCabinetMonitoringModuleNode] = {}
        """Cabinet monitoring module nodes."""

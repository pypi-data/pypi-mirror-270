import enum

import shv

from ..node._node import (
    SHVNode,
    SHVPropertyNode,
    SHVPropertySetterNode,
    SHVStatusNode
)


###############################################################################
# SYSTEM
###############################################################################

class SHVSystemStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        SYSTEM_STARTED = 1 << 0
        """
        System has started up successfully and is running.
        """
        ERROR_INTERNAL_BATTERY = 1 << 24
        """
        PLC internal battery is depleted or unavailable.
        """
        ERROR_USER_DISK_SPACE_FULL = 1 << 25
        """
        PLC memory for logs and configuration files is full.
        """
        ERROR_POWERLINK_RING = 1 << 26
        """
        Powerlink ring connection problem.
        """
        ERROR_LOADING_CONFIGURATION = 1 << 27
        """
        Error occurred while loading PLC configuration
        (default settings have been loaded).
        """
        ERROR_NETWORK_RING = 1 << 28
        """
        Network ring connection problem.
        """

    class BitMask(enum.IntFlag):
        SYSTEM_STARTED = 1
        """
        System has started up successfully and is running.
        """
        ERROR_INTERNAL_BATTERY = 1 << 24
        """
        PLC internal battery is depleted or unavailable.
        """
        ERROR_USER_DISK_SPACE_FULL = 1 << 25
        """
        PLC memory for logs and configuration files is full.
        """
        ERROR_POWERLINK_RING = 1 << 26
        """
        Powerlink ring connection problem.
        """
        ERROR_LOADING_CONFIGURATION = 1 << 27
        """
        Error occurred while loading PLC configuration
        (default settings have been loaded).
        """
        ERROR_NETWORK_RING = 1 << 28
        """
        Network ring connection problem.
        """

    @classmethod
    def is_system_started(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.SYSTEM_STARTED,
            mask=cls.BitMask.SYSTEM_STARTED
            )

    @classmethod
    def is_error_internal_battery(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_INTERNAL_BATTERY,
            mask=cls.BitMask.ERROR_INTERNAL_BATTERY
            )

    @classmethod
    def is_error_user_disc_space_full(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_USER_DISK_SPACE_FULL,
            mask=cls.BitMask.ERROR_USER_DISK_SPACE_FULL
            )

    @classmethod
    def is_error_powerlink_ring(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_POWERLINK_RING,
            mask=cls.BitMask.ERROR_POWERLINK_RING
            )

    @classmethod
    def is_error_loading_configuration(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_LOADING_CONFIGURATION,
            mask=cls.BitMask.ERROR_LOADING_CONFIGURATION
            )

    @classmethod
    def is_error_network_ring(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_NETWORK_RING,
            mask=cls.BitMask.ERROR_NETWORK_RING
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.SYSTEM_STARTED:
                cls.is_system_started(status),
            cls.BitAlias.ERROR_INTERNAL_BATTERY:
                cls.is_error_internal_battery(status),
            cls.BitAlias.ERROR_USER_DISK_SPACE_FULL:
                cls.is_error_user_disc_space_full(status),
            cls.BitAlias.ERROR_NETWORK_RING:
                cls.is_error_network_ring(status),
            cls.BitAlias.ERROR_POWERLINK_RING:
                cls.is_error_powerlink_ring(status),
            cls.BitAlias.ERROR_LOADING_CONFIGURATION:
                cls.is_error_loading_configuration(status)
            }


class SHVSystemInfoNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.temp_cpu = SHVPropertyNode(path=f'{path}/tempCPU')
        """[REAL, °C] Temperature of the PLC CPU."""
        self.temp_plc = SHVPropertyNode(path=f'{path}/tempPLC')
        """[REAL, °C] Temperature of the PLC IO board (motherboard)."""
        self.memory_user_size = SHVPropertyNode(path=f'{path}/memoryUserSize')
        """[REAL, MB] Size of the user partition on the memory card."""
        self.memory_user_free = SHVPropertyNode(path=f'{path}/memoryUserFree')
        """[REAL, MB] Available size of user memory."""
        self.memory_dram_free = SHVPropertyNode(path=f'{path}/memoryDRAMFree')
        """[REAL, MB] Available PLC DRAM memory."""


class SHVSystemEthernetNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.mac = SHVPropertyNode(path=f'{path}/MAC')
        """[STRING] MAC address of the PLC."""
        self.ip = SHVPropertyNode(path=f'{path}/IP')
        """[STRING] IP address of the PLC."""
        self.subnet_mask = SHVPropertyNode(path=f'{path}/subnetMask')
        """[STRING] Subnet mask of the PLC."""
        self.gateway_ip = SHVPropertyNode(path=f'{path}/gatewayIP')
        """[STRING] Gateway IP address of the PLC."""
        self.host_name = SHVPropertyNode(path=f'{path}/hostName')
        """[STRING] Host name of the PLC."""


class SHVSystemDateTimeNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.ntp_client_active = SHVPropertyNode(
            path=f'{path}/NTPClientActive'
            )
        """[BOOL] Active time sync from the NTP server."""
        self.date_time = SHVPropertyNode(
            path=f'{path}/dateTime'
            )
        """[DATETIME] Current UTC date and time of the PLC system."""


class SHVSystemPLCModulesNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.error_plc_module = SHVPropertyNode(
            path=f'{path}/errorPLCModule'
            )
        """
        [BOOL] Error of B&R PLC hardware module.
        """
        self.error_plc_module_address = SHVPropertyNode(
            path=f'{path}/errorPLCModuleAddress'
            )
        """
        [STRING] Identification address of B&R PLC hardware module in error.
        """


class SHVSuperiorSystemStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        SLAVE = 0b00
        """
        Slave mode is switched on
        (system is controlled from the superior system).
        """
        STANDALONE_COMMUNICATION_ERROR = 0b01
        """
        Communication error with the superior system (heartbeat error).
        System is in autonomous mode (slave mode off).
        """
        STANDALONE_FORCED = 0b10
        """
        The superior system switched the slave mode off.
        """
        STANDALONE_NO_SUPERIOR_SYSTEM = 0b01100011  # 99
        """
        System is in the standalone mode, no superior system is present
        (default state).
        """

    class BitMask(enum.IntFlag):
        MODE = 0xFF  # bits 0-7
        """
        System mode in relation to the superior system.
        """

    @classmethod
    def is_slave(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.SLAVE,
            mask=cls.BitMask.MODE
            )

    @classmethod
    def is_standalone_communication_error(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STANDALONE_COMMUNICATION_ERROR,
            mask=cls.BitMask.MODE
            )

    @classmethod
    def is_standalone_forced(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STANDALONE_FORCED,
            mask=cls.BitMask.MODE
            )

    @classmethod
    def is_standalone_no_superior_system(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STANDALONE_NO_SUPERIOR_SYSTEM,
            mask=cls.BitMask.MODE
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.SLAVE:
                cls.is_slave(status),
            cls.BitAlias.STANDALONE_COMMUNICATION_ERROR:
                cls.is_standalone_communication_error(status),
            cls.BitAlias.STANDALONE_FORCED:
                cls.is_standalone_forced(status),
            cls.BitAlias.STANDALONE_NO_SUPERIOR_SYSTEM:
                cls.is_standalone_no_superior_system(status)
            }


class SHVSuperiorSystemControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVSuperiorSystemStatusNode(
            path=f'{path}/status'
            )
        """
        [DWORD] Superior system status.
        """
        self.slave_mode = SHVPropertyNode(
            path=f'{path}/slaveMode'
            )
        """
        [BOOL] PLC is in the slave mode and
        is controlled by the superior system.
        """
        self.wdt_counter_plc = SHVPropertyNode(
            path=f'{path}/wdtCounterPLC'
            )
        """
        [UINT] PLC counter of seconds.
        Increments every second, overflows at 0xFFFF to 0x0000.
        """
        self.wdt_counter_pc = SHVPropertySetterNode(
            path=f'{path}/wdtCounterPC'
            )
        """
        [UDINT] Unix timestamp from EYAS, PLC time syncronization.
        (detection of the connected superior system via the heartbeat).
        """

    async def set_slave_mode_on(self) -> shv.SHVType:
        """
        Switch the slave mode on. PLC is in the slave mode,
        the zone is controlled by the superior system.
        """
        return await self.call('setSlaveModeOn')

    async def set_slave_mode_off(self) -> shv.SHVType:
        """
        Switch the slave mode off. PLC is in the standalone mode,
        superior system does not control the zone.
        """
        return await self.call('setSlaveModeOff')


class SHVSystemControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVSystemStatusNode(
            path=f'{path}/status'
            )
        """[DWORD] System status."""
        self.plc_disconnected = SHVPropertySetterNode(
            path=f'{path}/plcDisconnected'
            )
        """[BOOL] PLC disconnected."""
        self.name = SHVPropertySetterNode(
            path=f'{path}/name'
            )
        """[STRING] System name."""
        self.version = SHVPropertySetterNode(
            path=f'{path}/version'
            )
        """[STRING] PLC software version."""
        self.device_id = SHVPropertySetterNode(
            path=f'{path}/deviceID'
            )
        """[STRING] Unique device ID of the PLC."""
        self.info = SHVSystemInfoNode(
            path=f'{path}/info'
            )
        """System information."""
        self.ethernet = SHVSystemEthernetNode(
            path=f'{path}/ethernet'
            )
        """System Ethernet settings."""
        self.datetime = SHVSystemDateTimeNode(
            path=f'{path}/datetime'
            )
        """System date and time."""
        self.pl_cmodules = SHVSystemPLCModulesNode(
            path=f'{path}/PLCmodules'
            )
        """PLC modules."""
        self.superior_system = SHVSuperiorSystemControlNode(
            path=f'{path}/superiorSystem'
            )
        """Superior system control."""

    async def cmd_reboot_system(self) -> shv.SHVType:
        """Reboot the PLC system."""
        return await self.call('cmdRebootSystem')

    async def cmd_reset_errors(self) -> shv.SHVType:
        """Reset all warnings and errors of the PLC system."""
        return await self.call('cmdResetErrors')


###############################################################################
# SYSTEM SAFETY
###############################################################################

class SHVSystemSafetyStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        STATE_UNKNOWN_NOT_RESPONDING = 0
        """
        System state is unknown. The SafeLogic controller is not responding
        (likely due to a communication error).
        """
        STATE_SAFETY_CPU_REPLACED = 1
        """
        The SafeLogic controller has been replaced (UDID mismatch detected).
        Operation "cmdAcknowledge" is required.
        """
        STATE_PREOPERATIONAL = 2
        """
        Diagnostics service on the SafeLogic controller is not activated yet
        (likely due to a new software is being uploaded or
        the "cmdAcknowledge" command is being processed).
        """
        STATE_STARTUP = 3
        """
        The SafeLogic controller is starting up.
        Safety software is not initialized yet.
        """
        STATE_INITIALIZATION = 4
        """
        Safety software is being initialized.
        """
        STATE_INVALID = 5
        """
        The safety system is invalid (likely due to the SafeKey has not been
        filled in or the The SafeLogic controller is still starting up).
        """
        STATE_NO_EXECUTION = 6
        """
        The safety software cannot be executed (likely no software has been
        uploaded, or the uploaded software is corrupted).
        """
        STATE_SAFEKEY_CHANGED = 7
        """
        The SafeKey has been changed. Operation "cmdAcknowledge" is required.
        """
        STATE_MODULE_FIRMWARE_CHANGED = 8
        """
        A SafeNode (a safety module) firmware has been changed.
        Operation "cmdAcknowledge" is required.
        """
        STATE_MODULE_REPLACED = 9
        """
        A SafeNode (a safety module) has been replaced (module UDID mismatch
        detected). Operation "cmdAcknowledge" is required.
        """
        STATE_MODULE_MISSING = 10
        """
        A SafeNode (a safety module) is missing.
        Module replacement is required.
        """
        STATE_FAILSAFE = 11
        """
        A non-specified failsafe state is detected (the state does not match
        any specific fail state, encoded in the safety system status).
        """
        STATE_DEBUG_HALT = 12
        """
        The SafeLogic controller is in a halted state for debugging
        (the halt command was issued from SafeDesigner).
        """
        STATE_DEBUG_STOP = 13
        """
        The SafeLogic controller has been stopped in DEBUG mode.
        This mode will be automatically exited after 10 minutes.
        """
        STATE_DEBUG_RUN = 14
        """
        The SafeLogic controller is currently running in DEBUG mode.
        This mode will be automatically exited after 10 minutes.
        """
        STATE_STOP = 15
        """
        The SafeLogic controller is currently not running.
        """
        STATE_RUNNING_SETUP_MODE = 16
        """
        The SafeLogic controller is currently running
        with the setup mode activated.
        """
        STATE_RUNNING = 17
        """
        The SafeLogic controller is currently running.
        All systems are functioning correctly.
        """
        CONNECTION_ACTIVE = 1 << 8
        """
        The SafeLogic controller is connected to the non-safety system
        and is able to send and receive data.
        """
        SW_DOWNLOAD_IN_PROGRESS = 1 << 9
        """
        The safety system is currently downloading new software.
        """
        ACKNOWLEDGE_IN_PROGRESS = 1 << 10
        """
        The acknowledge command ("cmdAcknowledge") is being processed.
        """
        ERROR_COMMUNICATION = 1 << 11
        """
        The SafeLogic controller is not responding to diagnostics queries.
        """

    class BitMask(enum.IntFlag):
        STATE = 0xFF  # bits 0-7
        """
        Current status of safety PLC.
        """
        CONNECTION_ACTIVE = 1 << 8
        """
        The SafeLogic controller is connected to the non-safety system
        and is able to send and receive data.
        """
        SW_DOWNLOAD_IN_PROGRESS = 1 << 9
        """
        The safety system is currently downloading new software.
        """
        ACKNOWLEDGE_IN_PROGRESS = 1 << 10
        """
        The acknowledge command ("cmdAcknowledge") is being processed.
        """
        ERROR_COMMUNICATION = 1 << 11
        """
        The SafeLogic controller is not responding to diagnostics queries.
        """
        MODULES_CHANGED_FW = 0xFF << 16  # bits 16-23
        """
        The number of hardware modules that have a changed firmware.
        """
        MODULES_REPLACED = 0xFF << 24  # bits 24-31
        """
        The number of hardware modules that have been replaced or are missing.
        """

    @classmethod
    def is_state_unknown_not_responding(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_UNKNOWN_NOT_RESPONDING,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_safety_cpu_replaced(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_SAFETY_CPU_REPLACED,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_preoperational(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_PREOPERATIONAL,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_startup(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_STARTUP,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_initialization(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_INITIALIZATION,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_invalid(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_INVALID,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_no_execution(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_NO_EXECUTION,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_safekey_changed(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_SAFEKEY_CHANGED,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_module_firmware_changed(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_MODULE_FIRMWARE_CHANGED,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_module_replaced(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_MODULE_REPLACED,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_module_missing(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_MODULE_MISSING,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_failsafe(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_FAILSAFE,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_debug_halt(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_DEBUG_HALT,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_debug_stop(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_DEBUG_STOP,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_debug_run(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_DEBUG_RUN,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_stop(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_STOP,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_running_setup_mode(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_RUNNING_SETUP_MODE,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_state_running(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.STATE_RUNNING,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_connection_active(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.CONNECTION_ACTIVE,
            mask=cls.BitMask.CONNECTION_ACTIVE
            )

    @classmethod
    def is_sw_download_in_progress(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.SW_DOWNLOAD_IN_PROGRESS,
            mask=cls.BitMask.SW_DOWNLOAD_IN_PROGRESS
            )

    @classmethod
    def is_acknowledge_in_progress(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ACKNOWLEDGE_IN_PROGRESS,
            mask=cls.BitMask.ACKNOWLEDGE_IN_PROGRESS
            )

    @classmethod
    def is_error_communication(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_COMMUNICATION,
            mask=cls.BitMask.ERROR_COMMUNICATION
            )

    @classmethod
    def how_many_modules_changed_fw(cls, status: int) -> int:
        return status & cls.BitMask.MODULES_CHANGED_FW

    @classmethod
    def how_many_modules_replaced(cls, status: int) -> int:
        return status & cls.BitMask.MODULES_REPLACED

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.STATE_UNKNOWN_NOT_RESPONDING:
                cls.is_state_unknown_not_responding(status),
            cls.BitAlias.STATE_SAFETY_CPU_REPLACED:
                cls.is_state_safety_cpu_replaced(status),
            cls.BitAlias.STATE_PREOPERATIONAL:
                cls.is_state_preoperational(status),
            cls.BitAlias.STATE_STARTUP:
                cls.is_state_startup(status),
            cls.BitAlias.STATE_INITIALIZATION:
                cls.is_state_initialization(status),
            cls.BitAlias.STATE_INVALID:
                cls.is_state_invalid(status),
            cls.BitAlias.STATE_NO_EXECUTION:
                cls.is_state_no_execution(status),
            cls.BitAlias.STATE_SAFEKEY_CHANGED:
                cls.is_state_safekey_changed(status),
            cls.BitAlias.STATE_MODULE_FIRMWARE_CHANGED:
                cls.is_state_module_firmware_changed(status),
            cls.BitAlias.STATE_MODULE_REPLACED:
                cls.is_state_module_replaced(status),
            cls.BitAlias.STATE_MODULE_MISSING:
                cls.is_state_module_missing(status),
            cls.BitAlias.STATE_FAILSAFE:
                cls.is_state_failsafe(status),
            cls.BitAlias.STATE_DEBUG_HALT:
                cls.is_state_debug_halt(status),
            cls.BitAlias.STATE_DEBUG_STOP:
                cls.is_state_debug_stop(status),
            cls.BitAlias.STATE_DEBUG_RUN:
                cls.is_state_debug_run(status),
            cls.BitAlias.STATE_STOP:
                cls.is_state_stop(status),
            cls.BitAlias.STATE_RUNNING_SETUP_MODE:
                cls.is_state_running_setup_mode(status),
            cls.BitAlias.STATE_RUNNING:
                cls.is_state_running(status),
            cls.BitAlias.CONNECTION_ACTIVE:
                cls.is_connection_active(status),
            cls.BitAlias.SW_DOWNLOAD_IN_PROGRESS:
                cls.is_sw_download_in_progress(status),
            cls.BitAlias.ACKNOWLEDGE_IN_PROGRESS:
                cls.is_acknowledge_in_progress(status),
            cls.BitAlias.ERROR_COMMUNICATION:
                cls.is_error_communication(status),
            }


class SHVSystemSafetyAuthorizationNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.auth_key_generated = SHVPropertySetterNode(
            path=f'{path}/authKeyGenerated'
            )
        """[INT] Generated safety PLC authorization PIN key."""
        self.auth_key_inserted = SHVPropertyNode(
            path=f'{path}/authKeyInserted'
            )
        """[INT] Safety PLC authorization PIN key inserted from SHV."""


class SHVSystemSafetyControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVSystemSafetyStatusNode(
            path=f'{path}/status'
            )
        """[DWORD] Safety system status."""
        self.project_name = SHVPropertyNode(
            path=f'{path}/projectName'
            )
        """[STRING] Name of the safety zone project."""
        self.project_crc = SHVPropertyNode(
            path=f'{path}/projectCRC'
            )
        """[STRING] PLC safety software control checksum."""
        self.build_date_time = SHVPropertyNode(
            path=f'{path}/buildDateTime'
            )
        """[DATETIME] PLC safety software build date and time."""
        self.authorization = SHVSystemSafetyAuthorizationNode(
            path=f'{path}/authorization'
            )
        """Safety system authorization."""

    async def cmd_download_sw(self, **kwargs) -> shv.SHVType:
        """Download the new safety software to the PLC."""
        return await self.call('cmdDownloadSW', **kwargs)

    async def cmd_acknowledge(self, **kwargs) -> shv.SHVType:
        """Acknowledge the non-operational safety state."""
        return await self.call('cmdAcknowledge', **kwargs)

    async def cmd_reboot(self, **kwargs) -> shv.SHVType:
        """Reboot the safety PLC system."""
        return await self.call('cmdReboot', **kwargs)

    async def cmd_get_info(self, **kwargs) -> shv.SHVType:
        """Get the safety PLC system software information."""
        return await self.call('cmdGetInfo', **kwargs)

import enum

from ..node._node import (
    SHVNode,
    SHVPropertyNode,
    SHVPropertySetterNode,
    SHVStatusNode
)


###############################################################################
# AWA
###############################################################################

class SHVAWAStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        ACTIVE_TRAM_COMMUNICATION = 1 << 0
        """
        Communication between the AWA wayside station and the vehicle
        is currently active.
        """
        ERROR_COMMUNICATION = 1 << 29
        """
        Communication error between the PLC and the AWA wayside station.
        (only for devices connected to safety hardware modules).        """

    class BitMask(enum.IntFlag):
        ACTIVE_TRAM_COMMUNICATION = 1 << 0
        """
        Communication between the AWA wayside station and the vehicle
        is currently active.
        """
        ERROR_COMMUNICATION = 1 << 29
        """
        Communication error between the PLC and the AWA wayside station.
        (only for devices connected to safety hardware modules).
        """

    @classmethod
    def is_active_tram_communication(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ACTIVE_TRAM_COMMUNICATION,
            mask=cls.BitMask.ACTIVE_TRAM_COMMUNICATION
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
            cls.BitAlias.ACTIVE_TRAM_COMMUNICATION:
                cls.is_active_tram_communication(status),
            cls.BitAlias.ERROR_COMMUNICATION:
                cls.is_error_communication(status),
            }


class SHVAWAControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVAWAStatusNode(path=f'{path}/status')
        """[DWORD] AWA status."""
        self.vehicle_detected = SHVPropertyNode(path=f'{path}/vehicleDetected')
        """[STRING] Detailed data from the last detected vehicle."""


###############################################################################
# DIGITAL (KEY SWITCH)
###############################################################################

class SHVKeySwitchStatusControlNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        RESET_PRESSED = 1 << 24
        """
        Reset button is active (pressed).
        """
        ERROR_INPUT = 1 << 29
        """
        Hardware input error
        (only for devices connected to safety hardware modules).
        """
        ERROR_INPUT_COMPL = 1 << 30
        """
        Complementarity error. Both complementary inputs return the same signal
        (both true or both false).
        """

    class BitMask(enum.IntFlag):
        RESET_PRESSED = 1 << 24
        """
        Reset button is active (pressed).
        """
        ERROR_INPUT = 1 << 29
        """
        Hardware input error
        (only for devices connected to safety hardware modules).
        """
        ERROR_INPUT_COMPL = 1 << 30
        """
        Complementarity error. Both complementary inputs return the same signal
        (both true or both false)
        (only for devices connected to safety hardware modules).
        """

    @classmethod
    def is_reset_pressed(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.RESET_PRESSED,
            mask=cls.BitMask.RESET_PRESSED
            )

    @classmethod
    def is_error_input(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_INPUT,
            mask=cls.BitMask.ERROR_INPUT
            )

    @classmethod
    def is_error_input_compl(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_INPUT_COMPL,
            mask=cls.BitMask.ERROR_INPUT_COMPL
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.RESET_PRESSED: cls.is_reset_pressed(status),
            cls.BitAlias.ERROR_INPUT: cls.is_error_input(status),
            cls.BitAlias.ERROR_INPUT_COMPL: cls.is_error_input_compl(status)
            }


class SHVKeySwitchButtonsStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        REQUEST_INPUT_ACTIVE_01 = 1 << 0
        REQUEST_INPUT_ACTIVE_02 = 1 << 1
        REQUEST_INPUT_ACTIVE_03 = 1 << 2
        REQUEST_INPUT_ACTIVE_04 = 1 << 3
        REQUEST_INPUT_ACTIVE_05 = 1 << 4
        REQUEST_INPUT_ACTIVE_06 = 1 << 5
        REQUEST_INPUT_ACTIVE_07 = 1 << 6
        REQUEST_INPUT_ACTIVE_08 = 1 << 7
        REQUEST_INPUT_ACTIVE_09 = 1 << 8
        REQUEST_INPUT_ACTIVE_10 = 1 << 9
        REQUEST_INPUT_ACTIVE_11 = 1 << 10
        REQUEST_INPUT_ACTIVE_12 = 1 << 11
        REQUEST_INPUT_ACTIVE_13 = 1 << 12
        REQUEST_INPUT_ACTIVE_14 = 1 << 13
        REQUEST_INPUT_ACTIVE_15 = 1 << 14
        REQUEST_INPUT_ACTIVE_16 = 1 << 15
        REQUEST_INPUT_ACTIVE_17 = 1 << 16
        REQUEST_INPUT_ACTIVE_18 = 1 << 17
        REQUEST_INPUT_ACTIVE_19 = 1 << 18
        REQUEST_INPUT_ACTIVE_20 = 1 << 19
        REQUEST_INPUT_ACTIVE_21 = 1 << 20
        REQUEST_INPUT_ACTIVE_22 = 1 << 21
        REQUEST_INPUT_ACTIVE_23 = 1 << 22
        REQUEST_INPUT_ACTIVE_24 = 1 << 23
        REQUEST_INPUT_ACTIVE_25 = 1 << 24
        REQUEST_INPUT_ACTIVE_26 = 1 << 25
        REQUEST_INPUT_ACTIVE_27 = 1 << 26
        REQUEST_INPUT_ACTIVE_28 = 1 << 27
        REQUEST_INPUT_ACTIVE_29 = 1 << 28
        REQUEST_INPUT_ACTIVE_30 = 1 << 29
        REQUEST_INPUT_ACTIVE_31 = 1 << 30
        REQUEST_INPUT_ACTIVE_32 = 1 << 31

    class BitMask(enum.IntFlag):
        REQUEST_INPUT_ACTIVE_01 = 1 << 0
        REQUEST_INPUT_ACTIVE_02 = 1 << 1
        REQUEST_INPUT_ACTIVE_03 = 1 << 2
        REQUEST_INPUT_ACTIVE_04 = 1 << 3
        REQUEST_INPUT_ACTIVE_05 = 1 << 4
        REQUEST_INPUT_ACTIVE_06 = 1 << 5
        REQUEST_INPUT_ACTIVE_07 = 1 << 6
        REQUEST_INPUT_ACTIVE_08 = 1 << 7
        REQUEST_INPUT_ACTIVE_09 = 1 << 8
        REQUEST_INPUT_ACTIVE_10 = 1 << 9
        REQUEST_INPUT_ACTIVE_11 = 1 << 10
        REQUEST_INPUT_ACTIVE_12 = 1 << 11
        REQUEST_INPUT_ACTIVE_13 = 1 << 12
        REQUEST_INPUT_ACTIVE_14 = 1 << 13
        REQUEST_INPUT_ACTIVE_15 = 1 << 14
        REQUEST_INPUT_ACTIVE_16 = 1 << 15
        REQUEST_INPUT_ACTIVE_17 = 1 << 16
        REQUEST_INPUT_ACTIVE_18 = 1 << 17
        REQUEST_INPUT_ACTIVE_19 = 1 << 18
        REQUEST_INPUT_ACTIVE_20 = 1 << 19
        REQUEST_INPUT_ACTIVE_21 = 1 << 20
        REQUEST_INPUT_ACTIVE_22 = 1 << 21
        REQUEST_INPUT_ACTIVE_23 = 1 << 22
        REQUEST_INPUT_ACTIVE_24 = 1 << 23
        REQUEST_INPUT_ACTIVE_25 = 1 << 24
        REQUEST_INPUT_ACTIVE_26 = 1 << 25
        REQUEST_INPUT_ACTIVE_27 = 1 << 26
        REQUEST_INPUT_ACTIVE_28 = 1 << 27
        REQUEST_INPUT_ACTIVE_29 = 1 << 28
        REQUEST_INPUT_ACTIVE_30 = 1 << 29
        REQUEST_INPUT_ACTIVE_31 = 1 << 30
        REQUEST_INPUT_ACTIVE_32 = 1 << 31

    @classmethod
    def is_request_input_active(cls, button_index: int, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias(1 << button_index),
            mask=cls.BitMask(1 << button_index)
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias(1 << i): cls.is_request_input_active(i, status)
            for i in range(32)
            }


class SHVKeySwitchControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVKeySwitchStatusControlNode(
            path=f'{path}/status'
            )
        """[DWORD] Key switch status."""
        self.buttons_status = SHVKeySwitchButtonsStatusNode(
            path=f'{path}/buttonsStatus'
            )
        """[DWORD] Key switch buttons status."""


###############################################################################
# DRR
###############################################################################

class SHVDRRTransceiverStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        ACTIVE_TRAM_COMMUNICATION = 1 << 1
        """
        Communication between the DRR transceiver and the vehicle
        is currently active.
        """
        ERROR_POWER = 1 << 27
        """
        DRR channel internal power source error.
        """
        ERROR_DISCONNECTED = 1 << 28
        """
        Error due to the transceiver not being connected to the DRR channel.
        """
        ERROR_OVERCURRENT = 1 << 29
        """
        Error due to overcurrent in the transceiver or the DRR channel.
        """
        ERROR_COMPLEMENTARITY = 1 << 30
        """
        Complementarity error in the transceiver or the DRR channel.
        """

    class BitMask(enum.IntFlag):
        ACTIVE_TRAM_COMMUNICATION = 1 << 1
        """
        Communication between the DRR transceiver and the vehicle
        is currently active.
        """
        ERROR_POWER = 1 << 27
        """
        DRR channel internal power source error.
        """
        ERROR_DISCONNECTED = 1 << 28
        """
        Error due to the transceiver not being connected to the DRR channel.
        """
        ERROR_OVERCURRENT = 1 << 29
        """
        Error due to overcurrent in the transceiver or the DRR channel.
        """
        ERROR_COMPLEMENTARITY = 1 << 30
        """
        Complementarity error in the transceiver or the DRR channel.
        """

    @classmethod
    def is_active_tram_communication(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ACTIVE_TRAM_COMMUNICATION,
            mask=cls.BitMask.ACTIVE_TRAM_COMMUNICATION
            )

    @classmethod
    def is_error_power(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_POWER,
            mask=cls.BitMask.ERROR_POWER
            )

    @classmethod
    def is_error_disconnected(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_DISCONNECTED,
            mask=cls.BitMask.ERROR_DISCONNECTED
            )

    @classmethod
    def is_error_overcurrent(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_OVERCURRENT,
            mask=cls.BitMask.ERROR_OVERCURRENT
            )

    @classmethod
    def is_error_complementarity(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_COMPLEMENTARITY,
            mask=cls.BitMask.ERROR_COMPLEMENTARITY
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.ACTIVE_TRAM_COMMUNICATION:
                cls.is_active_tram_communication(status),
            cls.BitAlias.ERROR_POWER:
                cls.is_error_power(status),
            cls.BitAlias.ERROR_DISCONNECTED:
                cls.is_error_disconnected(status),
            cls.BitAlias.ERROR_OVERCURRENT:
                cls.is_error_overcurrent(status),
            cls.BitAlias.ERROR_COMPLEMENTARITY:
                cls.is_error_complementarity(status),
            }


class SHVDRRTransceiverControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVDRRTransceiverStatusNode(path=f"{path}/status")
        """[DWORD] DRR transceiver status."""
        self.vehicle_detected = SHVPropertyNode(path=f"{path}/vehicleDetected")
        """[STRING] Detailed data from the last detected vehicle."""


class SHVDRRStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        ERROR_COMMUNICATION = 1 << 30
        """Communication error between the PLC and the DRR controller."""

    class BitMask(enum.IntFlag):
        ERROR_COMMUNICATION = 1 << 30
        """Communication error between the PLC and the DRR controller."""

    @classmethod
    def is_error_communication(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitMask.ERROR_COMMUNICATION,
            mask=cls.BitMask.ERROR_COMMUNICATION
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.ERROR_COMMUNICATION:
                cls.is_error_communication(status),
            }


class SHVDRRControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVDRRStatusNode(path=f"{path}/status")
        """[DWORD] DRR status."""
        self.transceiver: dict[str, SHVDRRTransceiverControlNode] = {}
        """DRR transceiver control nodes."""


###############################################################################
# ROUTING TABLE
###############################################################################

class SHVRoutingTableControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.data = SHVPropertySetterNode(path=f"{path}/data")
        """[STRING] Routing table CSV data."""


###############################################################################
# SPIE
###############################################################################

class SHVSPIELoopStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        ACTIVE_TRAM_COMMUNICATION = 1 << 0
        """
        Communication between the SPIE loop and the vehicle
        is currently active.
        """

    class BitMask(enum.IntFlag):
        ACTIVE_TRAM_COMMUNICATION = 1 << 0
        """
        Communication between the SPIE loop and the vehicle
        is currently active.
        """

    @classmethod
    def is_active_tram_communication(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ACTIVE_TRAM_COMMUNICATION,
            mask=cls.BitMask.ACTIVE_TRAM_COMMUNICATION
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.ACTIVE_TRAM_COMMUNICATION:
                cls.is_active_tram_communication(status),
            }


class SHVSPIELoopControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVSPIELoopStatusNode(path=f"{path}/status")
        """[DWORD] SPIE loop status."""
        self.vehicle_detected = SHVPropertyNode(path=f"{path}/vehicleDetected")
        """[STRING] Detailed data from the last detected vehicle."""


class SHVSPIEStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        ERROR_COMMUNICATION = 1 << 30
        """Communication error between the PLC and the SPIE controller."""

    class BitMask(enum.IntFlag):
        ERROR_COMMUNICATION = 1 << 30
        """Communication error between the PLC and the SPIE controller."""

    @classmethod
    def is_error_communication(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitMask.ERROR_COMMUNICATION,
            mask=cls.BitMask.ERROR_COMMUNICATION
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.ERROR_COMMUNICATION:
                cls.is_error_communication(status),
            }


class SHVSPIEControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVSPIEStatusNode(path=f"{path}/status")
        """[DWORD] SPIE status."""
        self.loop: dict[str, SHVSPIELoopControlNode] = {}
        """SPIE loop control nodes."""


###############################################################################
# VECOM
###############################################################################

class SHVVecomLoopStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        NORMAL_OPERATION = 1 << 0
        """
        Vecom loop is operating normally.
        """
        ACTIVE_TRAM_COMMUNICATION = 1 << 1
        """
        Communication between the Vecom loop and the vehicle
        is currently active.
        """
        ERROR_DISCONNECTED = 1 << 27
        """
        Loop transceiver disconnected from the Vecom controller.
        """
        ERROR_OPEN_LOOP = 1 << 28
        """
        Error due to the loop not being connected to any loop transceiver.
        """
        ERROR_LOW_SUPPLY = 1 << 29
        """
        Error due to the loop not being powered properly (low supply voltage).
        """
        ERROR_HARDWARE = 1 << 30
        """
        Loop or loop transceiver hardware error.
        """

    class BitMask(enum.IntFlag):
        NORMAL_OPERATION = 1 << 0
        """
        Vecom loop is operating normally.
        """
        ACTIVE_TRAM_COMMUNICATION = 1 << 1
        """
        Communication between the Vecom loop and the vehicle
        is currently active.
        """
        ERROR_DISCONNECTED = 1 << 27
        """
        Loop transceiver disconnected from the Vecom controller.
        """
        ERROR_OPEN_LOOP = 1 << 28
        """
        Error due to the loop not being connected to any loop transceiver.
        """
        ERROR_LOW_SUPPLY = 1 << 29
        """
        Error due to the loop not being powered properly (low supply voltage).
        """
        ERROR_HARDWARE = 1 << 30
        """
        Loop or loop transceiver hardware error.
        """

    @classmethod
    def is_active_tram_communication(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ACTIVE_TRAM_COMMUNICATION,
            mask=cls.BitMask.ACTIVE_TRAM_COMMUNICATION
            )

    @classmethod
    def is_error_disconnected(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_DISCONNECTED,
            mask=cls.BitMask.ERROR_DISCONNECTED
            )

    @classmethod
    def is_error_open_loop(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_OPEN_LOOP,
            mask=cls.BitMask.ERROR_OPEN_LOOP
            )

    @classmethod
    def is_error_low_supply(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_LOW_SUPPLY,
            mask=cls.BitMask.ERROR_LOW_SUPPLY
            )

    @classmethod
    def is_error_hardware(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_HARDWARE,
            mask=cls.BitMask.ERROR_HARDWARE
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.ACTIVE_TRAM_COMMUNICATION:
                cls.is_active_tram_communication(status),
            cls.BitAlias.ERROR_DISCONNECTED:
                cls.is_error_disconnected(status),
            cls.BitAlias.ERROR_OPEN_LOOP:
                cls.is_error_open_loop(status),
            cls.BitAlias.ERROR_LOW_SUPPLY:
                cls.is_error_low_supply(status),
            cls.BitAlias.ERROR_HARDWARE:
                cls.is_error_hardware(status),
            }


class SHVVecomLoopControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVVecomLoopStatusNode(path=f"{path}/status")
        """[DWORD] Vecom loop status."""
        self.vehicle_detected = SHVPropertyNode(path=f"{path}/vehicleDetected")
        """[STRING] Detailed data from the last detected vehicle."""


class SHVVecomStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        ERROR_COMMUNICATION = 1 << 30
        """Communication error between the PLC and the Vecom controller."""

    class BitMask(enum.IntFlag):
        ERROR_COMMUNICATION = 1 << 30
        """Communication error between the PLC and the Vecom controller."""

    @classmethod
    def is_error_communication(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitMask.ERROR_COMMUNICATION,
            mask=cls.BitMask.ERROR_COMMUNICATION
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.ERROR_COMMUNICATION:
                cls.is_error_communication(status),
            }


class SHVVecomControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVVecomStatusNode(path=f"{path}/status")
        """[DWORD] Vecom status."""
        self.loop: dict[str, SHVVecomLoopControlNode] = {}
        """Vecom loop control nodes."""


###############################################################################
# VETRA
###############################################################################

class SHVVetraStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        ACTIVE_TRAM_COMMUNICATION = 1 << 1
        """
        Communication between the Vetra wayside transceiver and the vehicle
        is currently active.
        """
        ERROR_COMMUNICATION = 1 << 30
        """
        Communication error between the PLC and the Vetra wayside transceiver.
        """

    class BitMask(enum.IntFlag):
        ACTIVE_TRAM_COMMUNICATION = 1 << 1
        """
        Communication between the Vetra wayside transceiver and the vehicle
        is currently active.
        """
        ERROR_COMMUNICATION = 1 << 30
        """
        Communication error between the PLC and the Vetra wayside transceiver.
        """

    @classmethod
    def is_active_tram_communication(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitMask.ACTIVE_TRAM_COMMUNICATION,
            mask=cls.BitMask.ACTIVE_TRAM_COMMUNICATION
            )

    @classmethod
    def is_error_communication(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitMask.ERROR_COMMUNICATION,
            mask=cls.BitMask.ERROR_COMMUNICATION
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.ACTIVE_TRAM_COMMUNICATION:
                cls.is_active_tram_communication(status),
            cls.BitAlias.ERROR_COMMUNICATION:
                cls.is_error_communication(status),
            }


class SHVVetraConfigNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.rssi_limit = SHVPropertySetterNode(path=f"{path}/rssiLimit")
        """
        [UINT] Received signal strength filter (values 0-69).
        Lower value means a greater reach.
        """


class SHVVetraControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVVetraStatusNode(path=f"{path}/status")
        """[DWORD] Vetra status."""
        self.vehicle_detected = SHVPropertyNode(path=f"{path}/vehicleDetected")
        """[STRING] Detailed data from the last detected vehicle."""
        self.config = SHVVetraConfigNode(path=f"{path}/config")
        """Vetra configuration."""

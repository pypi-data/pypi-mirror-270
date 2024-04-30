import enum

import shv

from ..node._node import (
    SHVNode,
    SHVPropertySetterNode,
    SHVStatusNode,
)


class SHVRouteStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        FREE = 0b0000
        """
        Route is FREE and is not blocked externally.
        """
        BUILD = 0b0001
        """
        Route is being built.
        """
        READY = 0b0011
        """
        Route has been built and is ready for the tram to enter.
        """
        RELEASE = 0b0101
        """
        Route is being released after the tram has left.
        """
        OCCUPIED = 0b0111
        """
        Route is occupied by a tram.
        """
        ERROR = 0b1111
        """
        Route is in an error state.
        """
        CAN_BE_REQUESTED = 1 << 8
        """
        Route is FREE and is not blocked externally,
        and all its elements are not claimed or occupied.
        """
        BLOCKED = 1 << 9
        """
        Route is externally blocked.
        """
        AUTO_REQUEST_ENABLED = 1 << 10
        """
        Route can be automatically requested (if possible),
        if the gate memory is free.
        """
        REJECTED_PME = 1 << 16
        """
        An electrical point machine in the route layout could not reach its
        desired position while the route was being built
        (lost position timeout occured).
        """
        REJECTED_BLOCKED = 20 << 16
        """
        Route is blocked externally or by a command from the HMI control panel.
        """
        REJECTED_GATE_CLOSED = 21 << 16
        """
        Route start gate is CLOSED,
        the Zone is not in the state of normal operation (NORM).
        """
        REJECTED_CANNOT_BE_CLAIMED = 22 << 16
        """
        One or more elements of the route layout cannot be claimed
        (for example, if they are already claimed for another route).
        """
        SPAD = 1 << 24
        """
        A SPAD (Signal Passed At Danger) event is detected on the route
        (all SPAD events are passed to and handled by the start gate
        corresponding to the route).
        """

    class BitMask(enum.IntFlag):
        STATE = 0b1111  # bits 0-3
        """
        Route state.
        """
        REJECTION_ENUM = 0xFF0000
        """
        Route request rejection reason code.
        """
        CAN_BE_REQUESTED = 1 << 8
        """
        Route is FREE and is not blocked externally,
        and all its elements are not claimed or occupied.
        """
        BLOCKED = 1 << 9
        """
        Route is externally blocked.
        """
        SPAD = 1 << 24
        """
        A SPAD (Signal Passed At Danger) event is detected on the route
        (all SPAD events are passed to and handled by the start gate
        corresponding to the route).
        """

    @classmethod
    def is_free(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.FREE,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_build(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.BUILD,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_ready(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.READY,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_release(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.RELEASE,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_occupied(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.OCCUPIED,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_error(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR,
            mask=cls.BitMask.STATE
            )

    @classmethod
    def is_can_be_requested(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.CAN_BE_REQUESTED,
            mask=cls.BitMask.CAN_BE_REQUESTED
            )

    @classmethod
    def is_blocked(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.BLOCKED,
            mask=cls.BitMask.BLOCKED
            )

    @classmethod
    def is_rejected(cls, status: int) -> bool:
        return not cls.is_status_equal(
            status=status,
            equal_to=0,
            mask=cls.BitMask.REJECTION_ENUM
            )

    @classmethod
    def is_rejected_pme(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.REJECTED_PME,
            mask=cls.BitMask.REJECTION_ENUM
            )

    @classmethod
    def is_rejected_blocked(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.REJECTED_BLOCKED,
            mask=cls.BitMask.REJECTION_ENUM
            )

    @classmethod
    def is_rejected_gate_closed(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.REJECTED_GATE_CLOSED,
            mask=cls.BitMask.REJECTION_ENUM
            )

    @classmethod
    def is_rejected_cannot_be_claimed(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.REJECTED_CANNOT_BE_CLAIMED,
            mask=cls.BitMask.REJECTION_ENUM
            )

    @classmethod
    def is_spad(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.SPAD,
            mask=cls.BitMask.SPAD
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        resp = {
            cls.BitAlias.FREE:
                cls.is_free(status),
            cls.BitAlias.BUILD:
                cls.is_build(status),
            cls.BitAlias.READY:
                cls.is_ready(status),
            cls.BitAlias.RELEASE:
                cls.is_release(status),
            cls.BitAlias.OCCUPIED:
                cls.is_occupied(status),
            cls.BitAlias.ERROR:
                cls.is_error(status),
            cls.BitAlias.CAN_BE_REQUESTED:
                cls.is_can_be_requested(status),
            cls.BitAlias.BLOCKED:
                cls.is_blocked(status),
            cls.BitAlias.REJECTED_PME:
                cls.is_rejected_pme(status),
            cls.BitAlias.REJECTED_BLOCKED:
                cls.is_rejected_blocked(status),
            cls.BitAlias.REJECTED_GATE_CLOSED:
                cls.is_rejected_gate_closed(status),
            cls.BitAlias.REJECTED_CANNOT_BE_CLAIMED:
                cls.is_rejected_cannot_be_claimed(status),
            cls.BitAlias.SPAD:
                cls.is_spad(status)
                }
        return resp


class SHVRouteControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVRouteStatusNode(path=f'{path}/status')
        """[DWORD] Route status."""
        self.tram_id = SHVPropertySetterNode(path=f'{path}/tramID')
        """[UDINT] ID number of the vehicle currently occupying the route."""

    async def request(self, **kwargs) -> shv.SHVType:
        """Request the route."""
        return await self.call('request', **kwargs)

    async def enable_auto_request(self, **kwargs) -> shv.SHVType:
        """Enable automatic route request."""
        return await self.call('enableAutoRequest', **kwargs)

    async def disable_auto_request(self, **kwargs) -> shv.SHVType:
        """Disable automatic route request."""
        return await self.call('disableAutoRequest', **kwargs)

    async def start_gate(self, **kwargs) -> shv.SHVType:
        """Get the name of the start gate of the route."""
        return await self.call('startGate', **kwargs)

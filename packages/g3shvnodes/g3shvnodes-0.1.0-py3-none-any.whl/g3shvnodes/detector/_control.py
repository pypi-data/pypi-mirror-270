import enum

from ..node._node import SHVNode, SHVStatusNode


class SHVDetectorStatusNode(SHVStatusNode):
    class BitAlias(enum.IntFlag):
        FREE = 0b00
        """
        Detector is currently free.
        """
        OCCUPIED = 0b01
        """
        Detector is currently occupied.
        """
        CLAIMED = 0b10
        """
        Detector is currently claimed (reserved) for any route.
        """
        ERROR_INPUT = 1 << 29
        """
        Detector hardware input error
        (used only for devices connected to safety hardware modules).
        """
        ERROR_INPUT_COMPL = 1 << 30
        """
        Detector hardware input complementarity error. Both NO and NC
        complementary inputs return the same signal (both TRUE or both FALSE).
        """

    class BitMask(enum.IntFlag):
        STATE = (1 << 0) + (1 << 29) + (1 << 30)
        """
        Detector state (free / occupied / error).
        """
        CLAIMED = 1 << 1
        """
        Detector is currently claimed (reserved) for any route.
        """
        ERROR_INPUT = 1 << 29
        """
        Detector hardware input error.
        """
        ERROR_INPUT_COMPL = 1 << 30
        """
        Detector hardware input complementarity error. Both NO and NC
        complementary inputs return the same signal (both TRUE or both FALSE).
        """

    @classmethod
    def is_free(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.FREE,
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
    def is_claimed(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.CLAIMED,
            mask=cls.BitMask.CLAIMED
            )

    @classmethod
    def is_error(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_INPUT,
            mask=cls.BitMask.ERROR_INPUT
            )

    @classmethod
    def is_error_compl(cls, status: int) -> bool:
        return cls.is_status_equal(
            status=status,
            equal_to=cls.BitAlias.ERROR_INPUT_COMPL,
            mask=cls.BitMask.ERROR_INPUT_COMPL
            )

    @classmethod
    def inspect(cls, status: int) -> dict[BitAlias, bool]:  # type: ignore
        return {
            cls.BitAlias.FREE: cls.is_free(status),
            cls.BitAlias.OCCUPIED: cls.is_occupied(status),
            cls.BitAlias.CLAIMED: cls.is_claimed(status),
            cls.BitAlias.ERROR_INPUT: cls.is_error(status),
            cls.BitAlias.ERROR_INPUT_COMPL: cls.is_error_compl(status)
            }


class SHVDetectorControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.status = SHVDetectorStatusNode(path=f'{path}/status')
        """[DWORD] Detector status."""

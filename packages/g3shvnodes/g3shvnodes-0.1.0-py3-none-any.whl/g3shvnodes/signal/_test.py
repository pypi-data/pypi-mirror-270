import shv

from ..node._node import (
    SHVNode,
    SHVPropertyNode
)


###############################################################################
# SIGNAL
##############################################################################

class SHVSignalSymbolTestNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.symbol_off = SHVPropertyNode(path=f'{path}/symbolOff')
        """[BOOL] Symbol is switched OFF."""
        self.symbol_shining = SHVPropertyNode(path=f'{path}/symbolShining')
        """[BOOL] Symbol is switched ON (shining)."""
        self.current = SHVPropertyNode(path=f'{path}/current')
        """[INT, mA] Actual current in the symbol."""

    async def set_minimum_current(self, **kwargs) -> shv.SHVType:
        """Activate the minimum current (even if the symbol is OFF)."""
        return await self.call('setMinimumCurrent', **kwargs)

    async def set_warning(self, **kwargs) -> shv.SHVType:
        """Set the current in the symbol to the warning level."""
        return await self.call('setWarning', **kwargs)

    async def set_error(self, **kwargs) -> shv.SHVType:
        """Set the current in the symbol to the error level."""
        return await self.call('setError', **kwargs)

    async def reset(self, **kwargs) -> shv.SHVType:
        """Reset all error and warning states on the symbol."""
        return await self.call('reset', **kwargs)

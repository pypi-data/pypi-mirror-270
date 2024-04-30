import shv

from ..node._node import (
    SHVPropertyNode,
    SHVNode
)


class SHVSystemTestNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.test_running = SHVPropertyNode(
            path=f'{path}/testRunning'
            )
        """[BOOL] Any test is running."""
        self.superior_system_active = SHVPropertyNode(
            path=f'{path}/superiorSystemActive'
            )
        """[BOOL] EYAS simulation active. System heartbeat is running."""
        self.version = SHVPropertyNode(
            path=f'{path}/version'
            )
        """[STRING] PLC software version."""

    async def start_test(self, **kwargs) -> shv.SHVType:
        """Start a new test."""
        return await self.call('startTest', **kwargs)

    async def stop_test(self, **kwargs) -> shv.SHVType:
        """Stop the running test."""
        return await self.call('stopTest', **kwargs)

    async def superior_system_enable(self, **kwargs) -> shv.SHVType:
        """Enable system heartbeat (EYAS simulation)."""
        return await self.call('superiorSystemEnable', **kwargs)

    async def superior_system_disable(self, **kwargs) -> shv.SHVType:
        """Disable system heartbeat (EYAS simulation)."""
        return await self.call('superiorSystemDisable', **kwargs)

    async def reset_all(self, **kwargs) -> shv.SHVType:
        """Reset all test devices to default state."""
        return await self.call('resetAll', **kwargs)

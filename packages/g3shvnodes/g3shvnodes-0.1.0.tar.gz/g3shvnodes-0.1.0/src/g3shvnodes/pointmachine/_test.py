import shv

from ..node._node import (
    SHVNode,
    SHVPropertyNode,
    SHVPropertySetterNode
)


class _SHVPMTestNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.position_left = SHVPropertyNode(
            path=f'{path}/positionLeft'
            )
        """[BOOL] Point machine is in position LEFT."""
        self.position_right = SHVPropertyNode(
            path=f'{path}/positionRight'
            )
        """[BOOL] Point machine is in position RIGHT."""
        self.position_middle = SHVPropertyNode(
            path=f'{path}/positionMiddle'
            )
        """[BOOL] Point machine is in position MIDDLE."""
        self.switching_blocked = SHVPropertyNode(
            path=f'{path}/switchingBlocked'
            )
        """
        [BOOL] Point machine switching is blocked by an extrernal obstacle.
        """
        self.rod_inserted = SHVPropertyNode(
            path=f'{path}/rodInserted'
            )
        """
        [BOOL] Rod for manual switching is inserted into point machine socket.
        """
        self.motor_moving = SHVPropertySetterNode(
            path=f'{path}/motorMoving'
            )
        """
        [BOOL] Point machine motor is moving.
        """
        self.switch_time = SHVPropertySetterNode(
            path=f'{path}/switchTime'
            )
        """
        [INT, ms] Point machine switch time (by the motor).
        """

    async def reset(self, **kwargs) -> shv.SHVType:
        """
        Reset a point machine test twin to the default state:
        - position is LEFT;
        - no rod for manual switching in socket;
        - point machine is not blocked;
        - no position sensors' error.
        """
        return await self.call('reset', **kwargs)

    async def insert_rod(self, **kwargs) -> shv.SHVType:
        """
        Insert a rod for manual switching into the point machine's socket.
        """
        return await self.call('insertRod', **kwargs)

    async def remove_rod(self, **kwargs) -> shv.SHVType:
        """
        Remove the rod for manual switching from the point machine's socket.
        """
        return await self.call('removeRod', **kwargs)

    async def set_position_left(self, **kwargs) -> shv.SHVType:
        """
        Insert a rod for manual switching into the point machine's socket
        and manually switch the point machine to the LEFT position.
        """
        return await self.call('setPositionLeft', **kwargs)

    async def set_position_right(self, **kwargs) -> shv.SHVType:
        """
        Insert a rod for manual switching into the point machine's socket
        and manually switch the point machine to the RIGHT position.
        """
        return await self.call('setPositionRight', **kwargs)

    async def set_position_middle(self, **kwargs) -> shv.SHVType:
        """
        Insert a rod for manual switching into the point machine's socket
        and manually switch the point machine to the MIDDLE position.
        """
        return await self.call('setPositionMiddle', **kwargs)

    async def set_switch_block(self, **kwargs) -> shv.SHVType:
        """
        Insert an external virtual obstacle into the switching mechanism of
        the point machine, so it is blocked against switching.
        """
        return await self.call('setSwitchBlock', **kwargs)

    async def reset_switch_block(self, **kwargs) -> shv.SHVType:
        """
        Remove the external virtual obstacle from the switching mechanism of
        the point machine, so it is able to switch.
        """
        return await self.call('resetSwitchBlock', **kwargs)

    async def set_flood_mechanical(self, **kwargs) -> shv.SHVType:
        """
        Simulate flooding of the mechanical part of the point machine.
        """
        return await self.call('setFloodMechanical', **kwargs)

    async def set_flood_electrical(self, **kwargs) -> shv.SHVType:
        """
        Simulate flooding of the electrical part of the point machine.
        """
        return await self.call('setFloodElectrical', **kwargs)

    async def set_cover_electrical(self, **kwargs) -> shv.SHVType:
        """
        Simulate opening the cover of the electrical part of the point machine.
        """
        return await self.call('setCoverElectrical', **kwargs)

    async def set_cover_mechanical(self, **kwargs) -> shv.SHVType:
        """
        Simulate opening the cover of the mechanical part of the point machine.
        """
        return await self.call('setCoverMechanical', **kwargs)


class SHVPMMTestNode(_SHVPMTestNode):
    pass


class SHVPMETestNode(_SHVPMTestNode):
    pass

import shv

from ..node._node import (
    SHVNode,
    SHVPropertyNode,
    SHVPropertySetterNode,
)


###############################################################################
# HEATING - CONTACTOR ROD
###############################################################################

class SHVHeatingContactorRodTestNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.heating_active = SHVPropertyNode(path=f'{path}/heatingActive')
        """[BOOL] Heating rod is active and heating."""
        self.heating_off = SHVPropertyNode(path=f'{path}/heatingOff')
        """[BOOL] Heating rod is switched off."""
        self.current = SHVPropertyNode(path=f'{path}/current')
        """[REAL, A] Electrical current in heating rod in mA."""

    async def set_break(self, **kwargs) -> shv.SHVType:
        """Break heating rod completely (no current)."""
        return await self.call('setBreak', **kwargs)

    async def set_break_partial(self, **kwargs) -> shv.SHVType:
        """Break heating rod partially."""
        return await self.call('setBreakPartial', **kwargs)

    async def set_short(self, **kwargs) -> shv.SHVType:
        """Short-circuit heating rod completely."""
        return await self.call('setShort', **kwargs)

    async def set_short_partial(self, **kwargs) -> shv.SHVType:
        """Short-circuit heating rod partially."""
        return await self.call('setShortPartial', **kwargs)

    async def reset(self, **kwargs) -> shv.SHVType:
        """Reset heating rod to default state."""
        return await self.call('reset', **kwargs)


###############################################################################
# HEATING METEO
###############################################################################

class SHVHeatingMeteoTestNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.meteo_heating_active = SHVPropertyNode(
            path=f'{path}/meteoHeatingActive'
            )
        """[BOOL] Heating of the meteo unit is active."""
        self.temp_air = SHVPropertySetterNode(
            path=f'{path}/tempAir'
            )
        """[REAL, °C] Measured ambient air temperature."""
        self.temp_rail = SHVPropertySetterNode(
            path=f'{path}/tempRail'
            )
        """[REAL, °C] Measured rail temperature."""
        self.temp_meteo = SHVPropertySetterNode(
            path=f'{path}/tempMeteo'
            )
        """[REAL, °C] Measured temperature of the meteo unit."""

    async def set_wet(self, **kwargs) -> shv.SHVType:
        """Set meteo conditions to wet."""
        return await self.call('setWet', **kwargs)

    async def set_dry(self, **kwargs) -> shv.SHVType:
        """Set meteo conditions to dry."""
        return await self.call('setDry', **kwargs)

    async def reset(self, **kwargs) -> shv.SHVType:
        """Reset the meteo unit to the default state."""
        return await self.call('reset', **kwargs)

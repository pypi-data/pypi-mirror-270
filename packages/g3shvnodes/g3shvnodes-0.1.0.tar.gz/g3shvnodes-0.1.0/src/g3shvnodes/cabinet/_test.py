import shv

from ..node._node import (
    SHVPropertySetterNode,
    SHVPropertyNode,
    SHVNode,
    SHVDigitalOutputTestNode
)


###############################################################################
# CABINET - UPS
###############################################################################

class SHVCabinetUPSTestNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.inhibit = SHVPropertyNode(path=f'{path}/inhibit')
        """[BOOL] UPS inhibit output from the control PLC is active."""

    async def set_buffering(self, **kwargs) -> shv.SHVType:
        """Set buffering from batteries on the UPS unit."""
        return await self.call('setBuffering', **kwargs)

    async def set_ready(self, **kwargs) -> shv.SHVType:
        """Set ready output on UPS unit."""
        return await self.call('setReady', **kwargs)

    async def set_replace_battery(self, **kwargs) -> shv.SHVType:
        """Set replace battery output on UPS unit."""
        return await self.call('setReplaceBattery', **kwargs)

    async def reset(self, **kwargs) -> shv.SHVType:
        """Reset UPS to the default state (everything OK, running from net)."""
        return await self.call('reset', **kwargs)


###############################################################################
# CABINET - FUSE
###############################################################################

class SHVCabinetFuseTestNode(SHVDigitalOutputTestNode):
    pass


###############################################################################
# CABINET - CONVERTOR
###############################################################################

class SHVCabinetConvertorTestNode(SHVDigitalOutputTestNode):
    pass


###############################################################################
# CABINET - PANEL
###############################################################################

class SHVCabinetPanelTestNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.shining_norm = SHVPropertyNode(
            path=f'{path}/shiningNORM'
            )
        """[BOOL] LED for the NORM state is shining."""
        self.shining_ab = SHVPropertyNode(
            path=f'{path}/shiningAB'
            )
        """[BOOL] LED for the AB state is shining."""
        self.shining_ei = SHVPropertyNode(
            path=f'{path}/shiningEI'
            )
        """[BOOL] LED for the EI state is shining."""
        self.shining_calibration = SHVPropertyNode(
            path=f'{path}/shiningCalibration'
            )
        """[BOOL] LED for calibration active is shining."""

    async def press_norm(self, **kwargs) -> shv.SHVType:
        """Press button NORM."""
        return await self.call('pressNorm', **kwargs)

    async def press_ab(self, **kwargs) -> shv.SHVType:
        """Press button AB."""
        return await self.call('pressAB', **kwargs)

    async def press_ei(self, **kwargs) -> shv.SHVType:
        """Press button EI."""
        return await self.call('pressEI', **kwargs)

    async def press_calibration(self, **kwargs) -> shv.SHVType:
        """Press button to activate calibration."""
        return await self.call('pressCalibration', **kwargs)

    async def reset(self, **kwargs) -> shv.SHVType:
        """Reset all digital inputs and outputs on the cabinet panel
        to the default state.
        """
        return await self.call('reset', **kwargs)


###############################################################################
# CABINET
###############################################################################


class SHVCabinetTestNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.fan_active = SHVPropertyNode(
            path=f'{path}/fanActive'
            )
        """[BOOL] Switch internal fan active."""
        self.internal_light_active = SHVPropertyNode(
            path=f'{path}/internalLightActive'
            )
        """[BOOL] Switch internal cabinet lightning active."""
        self.night_mode_active = SHVPropertyNode(
            path=f'{path}/nightModeActive'
            )
        """
        [BOOL] Night mode is on (input from twilight sensor from control PLC).
        """
        self.voltage24_v = SHVPropertySetterNode(
            path=f'{path}/24V'
            )
        """[REAL, V] Actual voltage at the 24V bus."""
        self.catenary_voltage = SHVPropertySetterNode(
            path=f'{path}/catenaryVoltage'
            )
        """[REAL, V] Actual catenary (OCL) voltage."""
        self.temperature = SHVPropertySetterNode(
            path=f'{path}/temperature'
            )
        """[REAL, °C] Actual temperature in the upper part of the cabinet."""
        self.temperature_bottom = SHVPropertySetterNode(
            path=f'{path}/temperatureBottom'
            )
        """[REAL, °C] Actual temperature in the bottom part of the cabinet."""
        self.panel = SHVCabinetPanelTestNode(
            path=f'{path}/temperatureBottom'
            )
        """Cabinet panel test node."""

    async def set_door_open(self, **kwargs) -> shv.SHVType:
        """Open the cabinet door."""
        return await self.call('setDoorOpen', **kwargs)

    async def set_door_closed(self, **kwargs) -> shv.SHVType:
        """Close the cabinet door."""
        return await self.call('setDoorClosed', **kwargs)

    async def set_day_mode(self, **kwargs) -> shv.SHVType:
        """Deactivate twilight sensor output - simulate day."""
        return await self.call('setDayMode', **kwargs)

    async def set_night_mode(self, **kwargs) -> shv.SHVType:
        """Activate twilight sensor output - simulate night."""
        return await self.call('setNightMode', **kwargs)

    async def set_error_ring(self, **kwargs) -> shv.SHVType:
        """Simulate ethernet ring error."""
        return await self.call('setErrorRing', **kwargs)

    async def reset_error_ring(self, **kwargs) -> shv.SHVType:
        """Reset ethernet ring error."""
        return await self.call('resetErrorRing', **kwargs)

    async def set_catenary_voltage_present(self, **kwargs) -> shv.SHVType:
        """Activate digital output for catenary voltage."""
        return await self.call('setCatenaryVoltagePresent', **kwargs)

    async def reset_catenary_voltage_present(self, **kwargs) -> shv.SHVType:
        """Deactivate output for catenary voltage."""
        return await self.call('resetCatenaryVoltagePresent', **kwargs)

    async def set_voltage_230V_present(self, **kwargs) -> shv.SHVType:
        """Activate output for 230V."""
        return await self.call('set230VPresent', **kwargs)

    async def reset_voltage_230V_present(self, **kwargs) -> shv.SHVType:
        """Deactivate output for 230V."""
        return await self.call('reset230VPresent', **kwargs)

    async def reset(self, **kwargs) -> shv.SHVType:
        """Reset cabinet to the default state."""
        return await self.call('reset', **kwargs)

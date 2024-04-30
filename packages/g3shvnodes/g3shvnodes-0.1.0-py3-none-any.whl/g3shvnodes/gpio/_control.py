from ..node._node import SHVNode, SHVPropertyNode


class SHVGPIOControlNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.inputs = SHVPropertyNode(path=f'{path}/inputs')
        """[DWORD] Bitfield of 32 inputs to PLC (project specific)."""
        self.outputs = SHVPropertyNode(path=f'{path}/outputs')
        """[DWORD] Bitfield of 32 outputs from PLC (project specific)."""

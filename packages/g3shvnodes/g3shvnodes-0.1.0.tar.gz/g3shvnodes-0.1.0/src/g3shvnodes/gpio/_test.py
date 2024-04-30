from ..node._node import (
    SHVNode,
    SHVDigitalOutputTestNode,
    SHVDigitalInputTestNode
)


class SHVGPIOInputTestNode(SHVDigitalOutputTestNode):
    pass


class SHVGPIOOutputTestNode(SHVDigitalInputTestNode):
    pass


class SHVGPIOTestNode(SHVNode):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.inputs: dict[str, SHVGPIOInputTestNode] = {}
        """GPIO input test nodes."""
        self.outputs: dict[str, SHVGPIOOutputTestNode] = {}
        """GPIO output test nodes."""

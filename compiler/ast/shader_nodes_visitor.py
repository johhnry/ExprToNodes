import bpy
import mathutils

from .ast_visitor import ASTVisitor
from .bin_op import BinOp
from .number import Number


class ShaderNodesVisitor(ASTVisitor):
    def __init__(self):
        self.node_tree = bpy.data.materials[0].node_tree
        self.location = mathutils.Vector((0.0, 0.0))
        self.nodes_offset = 50

    def set_input(self, node, input_index, input_node) -> None:
        input = node.inputs[input_index]
        if type(input_node) == float:
            input.default_value = input_node
        else:
            self.node_tree.links.new(input, input_node.outputs[0])

    def visit_BinOp(self, node: BinOp) -> bpy.types.ShaderNodeMath:
        math_node = self.node_tree.nodes.new("ShaderNodeMath")
        math_node.operation = node.blend_op

        math_node.location = self.location
        self.location -= mathutils.Vector((math_node.width + self.nodes_offset, 0.0))

        left_node = node.left.accept(self)
        right_node = node.right.accept(self)

        self.set_input(math_node, 0, left_node)
        self.set_input(math_node, 1, right_node)

        return math_node

    def visit_Number(self, node: Number) -> float:
        return node.value

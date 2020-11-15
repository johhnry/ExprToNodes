import bpy

from ..compiler.ast.shader_nodes_visitor import ShaderNodesVisitor
from ..compiler.parser.expr_parser import ExprParser
from .utils import check_if_node_tree


class EXPRTONODES_OT_Parse(bpy.types.Operator):
    bl_idname = "expr_to_nodes.parse"
    bl_label = "Parse the expression"

    def __init__(self):
        self.parser = ExprParser()
        self.parser.build()

    @classmethod
    def poll(cls, context):
        return check_if_node_tree(context)

    def execute(self, context):
        expression = context.scene.expr_to_nodes.expression
        active_material = context.active_object.active_material

        nodes_visitor = ShaderNodesVisitor(active_material.node_tree)
        ast = self.parser.parse(expression)

        ast.accept(nodes_visitor)

        context.scene.expr_to_nodes.expression = ""

        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

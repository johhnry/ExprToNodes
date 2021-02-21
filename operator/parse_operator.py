import bpy

from ..compiler.ast.shader_nodes_visitor import ShaderNodesVisitor
from ..compiler.parser.expr_parser import ExprParser
from . import utils


class EXPRTONODES_OT_Parse(bpy.types.Operator):
    bl_idname = "expr_to_nodes.parse"
    bl_label = "Parse the expression"
    bl_options = {"REGISTER", "UNDO"}

    # Focus on the field
    # https://blender.stackexchange.com/questions/118132/how-to-make-field-focused-in-props-dialog
    bl_property = "expression"

    # Used when opening the dialog
    expression: bpy.props.StringProperty()

    def __init__(self):
        self.parser = ExprParser()
        self.parser.build()

    @classmethod
    def poll(cls, context):
        return (
            utils.check_if_node_tree(context)
            or context.space_data.type == "TEXT_EDITOR"
        )

    def get_text_editor_selection(self, text):
        lines = text.lines

        begin_selection = 0
        min_line = min(text.current_line_index, text.select_end_line_index)
        max_line = max(text.current_line_index, text.select_end_line_index)
        for i in range(0, min_line):
            begin_selection += len(lines[i].body) + 1

        end_selection = begin_selection
        begin_selection += min(text.current_character, text.select_end_character)

        for i in range(min_line, max_line):
            end_selection += len(lines[i].body) + 1

        end_selection += max(text.current_character, text.select_end_character)

        return lines.data.as_string()[begin_selection:end_selection]

    def execute(self, context):
        expression = ""

        if utils.check_if_node_tree(context):
            expression = self.expression
        elif context.space_data.type == "TEXT_EDITOR":
            text = context.area.spaces[0].text

            if not text:
                self.report({"ERROR"}, "ExprToParse: no text file opened")
                return {"CANCELLED"}

            expression = self.get_text_editor_selection(text)

        if len(expression) == 0:
            self.report({"WARNING"}, "ExprToParse: Can't parse empty expression")
            return {"CANCELLED"}

        active_material = context.active_object.active_material

        nodes_visitor = ShaderNodesVisitor(active_material.node_tree)

        # try:
        ast = self.parser.parse(expression)
        """except Exception as e:
            self.report({"ERROR"}, "Parse error : {}".format(e))
            return {"CANCELLED"}"""

        ast.accept(nodes_visitor)

        self.report({"INFO"}, "ExprToParse: Compilation successfull")

        return {"FINISHED"}

    def invoke(self, context, event):
        if utils.check_if_node_tree(context):
            return context.window_manager.invoke_props_dialog(self, width=400)
        return self.execute(context)

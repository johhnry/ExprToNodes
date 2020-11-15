import bpy


class EXPRTONODES_PT_Main(bpy.types.Panel):
    bl_space_type = "TEXT_EDITOR"
    bl_label = "Expression to nodes"
    bl_region_type = "UI"
    bl_category = "Expr to nodes"

    def draw(self, context):
        layout = self.layout
        row = layout.column(align=True)
        scene = bpy.context.scene

        row.prop(scene.expr_to_nodes, "expression", text="Expression")
        row.separator()
        row.operator("expr_to_nodes.parse", text="Parse")

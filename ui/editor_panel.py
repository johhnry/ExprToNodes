import bpy


class EXPRTONODES_PT_Main(bpy.types.Panel):
    bl_space_type = "NODE_EDITOR"
    bl_label = "Expression to nodes"
    bl_region_type = "UI"
    bl_category = "Expr to nodes"

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)

        layout.label(text="This is a custom panel")

        row.prop(self, "text_input")

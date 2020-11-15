import bpy


class ExprToNodesProps(bpy.types.PropertyGroup):
    expression: bpy.props.StringProperty(
        name="Expression", description="Mathematical expression to parse", default=""
    )

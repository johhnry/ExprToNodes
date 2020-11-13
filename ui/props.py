import bpy


class ExprToNodesProps(bpy.types.PropertyGroup):
    text_input: bpy.props.StringProperty(name="Text input")

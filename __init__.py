# <pep8-80 compliant>

bl_info = {
    "name": "Expression to nodes",
    "author": "Joseph Henry",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "Node Editor toolbar or Shift+E",
    "description": "Parse and compile mathematical expression to shader nodes",
    "warning": "",
    "category": "Node",
}

import sys

# if "bpy" in locals():
#     import importlib

#     importlib.reload(ui)
#     importlib.reload(compiler)
# else:
# Catch exception when running tests
try:
    import bpy
except ImportError as e:
    pass

from .operator.parse_operator import EXPRTONODES_OT_Parse
from .ui.editor_panel import EXPRTONODES_PT_Main
from .ui.props import ExprToNodesProps

classes = (
    EXPRTONODES_OT_Parse,
    ExprToNodesProps,
    EXPRTONODES_PT_Main,
)


def register():
    from bpy.utils import register_class

    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.expr_to_nodes = bpy.props.PointerProperty(type=ExprToNodesProps)


def unregister():
    from bpy.utils import unregister_class

    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.expr_to_nodes


if __name__ == "__main__":
    register()

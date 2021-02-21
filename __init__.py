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

    from .operator.parse_operator import EXPRTONODES_OT_Parse
    from .ui.editor_panel import EXPRTONODES_PT_Main

    classes = (
        EXPRTONODES_OT_Parse,
        # EXPRTONODES_PT_Main,
    )
except ImportError as e:
    print(e)


addon_keymaps = []


def register():
    from bpy.utils import register_class

    for cls in classes:
        bpy.utils.register_class(cls)

    # keymaps
    addon_keymaps.clear()
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="Text", space_type="TEXT_EDITOR")
        kmi = km.keymap_items.new(
            EXPRTONODES_OT_Parse.bl_idname, type="RET", value="PRESS", ctrl=True
        )
        addon_keymaps.append((km, kmi))

        km = kc.keymaps.new(name="Node Editor", space_type="NODE_EDITOR")
        kmi = km.keymap_items.new(
            EXPRTONODES_OT_Parse.bl_idname, type="E", value="PRESS", shift=True
        )
        addon_keymaps.append((km, kmi))


def unregister():
    from bpy.utils import unregister_class

    for cls in classes:
        bpy.utils.unregister_class(cls)

    # keymaps
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()

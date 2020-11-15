import bpy


def check_if_node_tree(context):
    space = context.space_data
    valid_trees = ["ShaderNodeTree", "CompositorNodeTree", "TextureNodeTree"]

    valid = False
    if (
        space.type == "NODE_EDITOR"
        and space.node_tree is not None
        and space.tree_type in valid_trees
    ):
        valid = True

    return valid

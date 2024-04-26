__author__ = """Skelly FreeMoCap"""
__email__ = "info@freemocap.org"
__version__ = "v2023.10.1017"

#######################################################################
### Add-on to adapt the Freemocap Blender output. It can adjust the
### empties position, add a rig and a body mesh. The resulting rig
### and animation can be imported in platforms like Unreal Engine.
### The rig has a TPose as rest pose for easier retargeting.
### For best results, when the script is ran the empties should be
### forming a standing still pose with arms open similar to A or T Pose

### The body_mesh.ply file should be in the same folder as the
### Blender file before manually opening it.
#######################################################################
import logging
import sys
from pathlib import Path

PACKAGE_ROOT_PATH = str(Path(__file__).parent)

root = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)
logger = logging.getLogger(__name__)

bl_info = {
    'name': 'ajc27_freemocap_blender_addon',
    'author': 'ajc27',
    'version': (1, 1, 7),
    'blender': (3, 0, 0),
    'location': '3D Viewport > Sidebar > Freemocap Adapter',
    'description': 'Add-on to adapt the Freemocap Blender output',
    'category': 'Development',
}


def unregister():
    import bpy

    print(f"Unregistering {__file__} as add-on")
    from .blender_interface import BLENDER_USER_INTERFACE_CLASSES
    for cls in BLENDER_USER_INTERFACE_CLASSES:
        print(f"Unregistering class {cls.__name__}")
        bpy.utils.unregister_class(cls)

    print(f"Unregistering property group FMC_ADAPTER_PROPERTIES")
    del bpy.types.Scene.fmc_adapter_properties


def register():
    import bpy

    print(f"Registering {__file__} as add-on")
    from .blender_interface import BLENDER_USER_INTERFACE_CLASSES
    print(f"Registering classes {BLENDER_USER_INTERFACE_CLASSES}")
    for cls in BLENDER_USER_INTERFACE_CLASSES:
        print(f"Registering class {cls.__name__}")
        bpy.utils.register_class(cls)

    print("Registering property group FMC_ADAPTER_PROPERTIES")

    from .blender_interface import FMC_ADAPTER_PROPERTIES
    bpy.types.Scene.fmc_adapter_properties = bpy.props.PointerProperty(type=FMC_ADAPTER_PROPERTIES)

    # try:
    #     from ajc27_freemocap_blender_addon.core_functions.fbx_export import get_io_scene_fbx_addon
    #     get_io_scene_fbx_addon()
    # except Exception as e:
    #     print(f"Error loading io_scene_fbx addon: {str(e)}")
    #     raise

    print(f"Finished registering {__file__} as add-on!")


if __name__ == "__main__":
    print(f"Running {__file__} as main file ")
    register()
    print(f"Finished running {__file__} as main file!")

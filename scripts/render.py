import sys
import os
import bpy
import random

# Detect operating system
is_windows = sys.platform == "win32"
is_macos = sys.platform == "darwin"

# Example paths for Blender 3.6 LTS
if is_windows:
    blender_python_path = r"C:\Program Files\Blender Foundation\Blender 3.6\3.6\python\lib\python3.10"
elif is_macos:
    blender_python_path = "/Applications/Blender.app/Contents/Resources/3.6/python/lib/python3.10"
else:
    # Add more cases for other operating systems if needed
    raise ValueError("Unsupported operating system")

# Add the path to Blender's Python to sys.path
sys.path.append(blender_python_path)

# Name
print("Abstract Art Generator by kennynahh and itsanantk")

# Accept the output path as a command-line argument (this is a CLI interface)
output_path = sys.argv[-1]
bpy.context.scene.render.filepath = output_path

# Clear scene
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Asset import (all obj files)
obj_path = "assets/obj"
obj_files = [f for f in os.listdir(obj_path) if f.endswith('.obj')]

# Set random sizes and positions for imported objects
for obj_file in obj_files:
    obj_file_path = os.path.join(obj_path, obj_file)
    bpy.ops.import_scene.obj(filepath=obj_file_path)

    # Get the last imported object (assuming it's the one just imported)
    imported_object = bpy.context.active_object

    # Set random scale (size) for the object
    scale_factor = random.uniform(0.1, 1.0)
    imported_object.scale = (scale_factor, scale_factor, scale_factor)

    # Set random position for the object
    imported_object.location = (
        random.uniform(-5, 5),
        random.uniform(-5, 5),
        random.uniform(0, 5)
    )

# Render
bpy.ops.render.render(write_still=True)

# Complete
print("Rendering is complete.")

# Run using the following CLI line while cd'd into the abstract-art-generator file (or open a terminal there):
# blender -b art.blend -P scripts/render.py
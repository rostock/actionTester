import bpy
import sys


path = 'text.obj'

bpy.ops.export_scene.obj(filepath=path, axis_forward='-Y', axis_up='Z', use_materials=True)

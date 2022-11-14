import bpy
import sys


path = 'text.obj'

bpy.ops.export_scene.fbx(filepath=path, axis_forward='-Z', axis_up='Y')

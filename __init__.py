# Blender addon that batch adjusts scene materials after importing FFXIV zones as fbx-files created with ZoneFBX.

# bl_info
bl_info = {
    "name" : "FFXIV Zones Adjustments",
    "author" : "jtabox",
    "description" : "Batch adjusts scene materials after importing FFXIV zones as fbx-files created with ZoneFBX.",
    "blender" : (2, 80, 0),
    "version" : (0, 2, 0),
    "location" : "3D View > Right Side Panel (N) > XIVZones",
    "warning" : "",
    "category" : "Material",
    "doc-url" : "https://github.com/jtabox/ffxiv-zones-adjustments"
}

# imports
import bpy

# draw the UI
class XIVZ_MainPanel(bpy.types.Panel):
    bl_label = "XIV Zones"
    bl_idname = "XIVZ_PT_MainPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "XIVZones"

    def draw(self, context):
        layout = self.layout
        layout.label(text = "FFXIV Zones Adjustments")
        row = layout.row()
        row = layout.row()
        row.operator("xivz.blend_mode_to_alpha_hashed", text = "Blend Mode To Alpha Hashed")
        row = layout.row()
        row.operator("xivz.fix_metallic_property", text = "Fix Materials Metallic Property")
        row = layout.row()
        row = layout.row()
        row.operator("xivz.normal_to_world_space", text = "Normal To World Space")
        row = layout.row()
        row.operator("xivz.normal_strength_to_half", text = "Normal Strength To Half")

# classes
class ChangeToAlphaHashed(bpy.types.Operator):
    bl_idname = "xivz.blend_mode_to_alpha_hashed"
    bl_label = "Blend Mode to Alpha Hashed"
    bl_description= "Changes the Alpha Blend mode for the viewport to Alpha Hashed"

    def execute(self, context):
        for item in bpy.data.materials:
            item.blend_method = 'HASHED'
        return {'FINISHED'}

class FixMetallicProperty(bpy.types.Operator):
    bl_idname = "xivz.fix_metallic_property"
    bl_label = "Fix Materials' Metallic Property"
    bl_description = "Removes the metallic property some materials are incorrectly exported with"
        
    def execute(self, context):
        for mat in bpy.data.materials:
            if not mat.use_nodes:
                mat.metallic = 0
                continue
            for n in mat.node_tree.nodes:
                if n.type == 'BSDF_PRINCIPLED':
                     n.inputs["Metallic"].default_value = 0  
        return {'FINISHED'}

class NormalToWorldSpace(bpy.types.Operator):
    bl_idname = "xivz.normal_to_world_space"
    bl_label = "Change Normal Maps to World Space"
    bl_description= "Changes Normal Maps' Shaders to World Space"
    
    def execute(self, context):
        for mat in bpy.data.materials:
            if mat.node_tree:
                for node in mat.node_tree.nodes:
                    if node.type == 'NORMAL_MAP':
                        node.space = 'WORLD'
        return {'FINISHED'}

class NormalStrengthToHalf(bpy.types.Operator):
    bl_idname = "xivz.normal_strength_to_half"
    bl_label = "Set Normal Map Strength to 50%"
    bl_description= "Sets Normal Map Shader Strength to 50%"
    
    def execute(self, context):
        for mat in bpy.data.materials:
            if mat.node_tree:
                for node in mat.node_tree.nodes:
                    if node.type == 'NORMAL_MAP':
                        node.inputs['Strength'].default_value = 0.5
        return {'FINISHED'}

classestoregister = (
    XIVZ_MainPanel,
    ChangeToAlphaHashed,
    FixMetallicProperty,
    NormalToWorldSpace,
    NormalStrengthToHalf)

def register():
    for cls in classestoregister:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classestoregister:
        bpy.utils.unregister_class(cls)
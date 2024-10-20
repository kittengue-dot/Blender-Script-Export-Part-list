import bpy
import csv

def export_selected_mesh_dimensions_to_csv(filepath):
    """Export Parts

    Args:
        filepath (str): Le chemin du fichier CSV de sortie.
    """

    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Part', 'Section X (mm)', 'Section Y (mm)', 'Length Z (mm)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for obj in bpy.context.selected_objects:
            if obj.type == 'MESH':
                
                dimensions = obj.dimensions

                x_dim = round(dimensions.x * 1000, 3)
                y_dim = round(dimensions.y * 1000, 3)
                z_dim = round(dimensions.z * 1000, 3)

                writer.writerow({'Part': obj.name, 'Section X (mm)': x_dim, 'Section Y (mm)': y_dim, 'Length Z (mm)': z_dim})

filepath = "/home/deltahedra/Documents/blender_part_list/part_list.csv"  # Replace destination path

export_selected_mesh_dimensions_to_csv(filepath)
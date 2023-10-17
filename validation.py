import numpy as np
from stl import mesh

# Assuming you have an STL file loaded in FreeCAD
# Replace 'your_mesh.stl' with the path to your STL file
stl_mesh = mesh.Mesh.from_file('simple_block_ascii.stl')

# Calculate the volume using numpy-stl
volume, cog, inertia = stl_mesh.get_mass_properties()

# Print the volume
surface_area = 0
for triangle in stl_mesh.vectors:
    # Calculate the vectors representing the edges of the triangle
    edge1 = triangle[1] - triangle[0]
    edge2 = triangle[2] - triangle[0]
    
    # Calculate the cross product of the edges to get the normal vector
    normal = np.cross(edge1, edge2)
    
    # Calculate the area of the triangle (half the magnitude of the cross product)
    area =  np.linalg.norm(normal)
    
    # Add the area to the total surface area
    surface_area += area

# Print the surface area

print("Surface area of the object: {} square units".format(surface_area))
print("Volume of the object: {} cubic units".format(volume))

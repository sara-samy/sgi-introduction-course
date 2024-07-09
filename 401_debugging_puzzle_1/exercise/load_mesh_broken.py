import os
import numpy as np

# This is a simple .obj file format parser. It does not handle all features of the format, 
# just the absolute most basic features. For real code, you use should use 
# `gpytoolbox.read_mesh()` or other libraries instead, this is just a basic example.

# THIS FUNCTION IS BROKEN! It has a small bug, your job is to find it and fix it.
#
# Fun fact: this buggy code was generated by ChatGPT 
def my_read_mesh_from_obj_file(obj_filename):

    # store the vertices and faces here
    vertices = []
    faces = []

    # open the file
    with open(obj_filename, 'r') as file:

        # walk through each line of the file
        for line in file:

            # if it starts with 'v', read a vertex
            if line.startswith('v '):
      
                # parse the line, discard the 'v', then read it into a list of 3 coordinates
                parts = line.strip().split()
                vertex = [float(coord) for coord in parts[1:4]]

                # add this vertex to the list of vertices
                vertices.append(vertex)

            # if it starts with 'f', read a vertex
            elif line.startswith('f '):

                # parse the line, discard the 'f', then read it into a list of 3 indices
                parts = line.strip().split()
                face = [int(index.split('/')[0]) for index in parts[1:]]
                
                # add this face to the list of faces
                faces.append(face)

   
    # The above code stores faces and vertices as lists-of-lists, but we usually 
    # work with numpy arrays. Convert them to numpy arrays.
    vertices = np.array(vertices)
    faces = np.array(faces)

    return vertices, faces

# Call the function on the mesh file sitting in this directory.
# Something is wrong with the resulting V,F!
# We promise nothing is wrong with this file itself.
V, F = my_read_mesh_from_obj_file("data/fox.obj")


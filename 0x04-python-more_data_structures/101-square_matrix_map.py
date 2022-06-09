#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda x:x, map(lambda z: [z[0]**2, z[1]**2, z[2]**2], matrix)))

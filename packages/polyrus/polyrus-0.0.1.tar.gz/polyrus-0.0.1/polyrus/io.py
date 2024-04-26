import numpy as np
import open3d as o3d

class IO:
    def __init__(self):
        pass

    @staticmethod
    def read_mesh(fname: str) -> o3d.cuda.pybind.geometry.TriangleMesh:
        mesh = o3d.io.read_triangle_mesh(fname)
        return mesh
    
    @staticmethod
    def read_mask(fname: str) -> np.array:
        mask = np.loadtxt(fname)
        return mask
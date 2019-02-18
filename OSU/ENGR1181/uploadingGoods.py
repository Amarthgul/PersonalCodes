import numpy as np;
import matplotlib.pyplot as plt;


def getCubeByAxis(offset = [0, 0, 0], xlen = 1, ylen = 1, zlen = 1):
    x = np.array([[offset[0], offset[0], offset[0] + xlen, offset[0] + xlen],
                   [offset[0], offset[0], offset[0] + xlen, offset[0] + xlen],
                   [offset[0], offset[0], offset[0] + xlen, offset[0] + xlen],
                   [offset[0], offset[0], offset[0] + xlen, offset[0] + xlen],
                   [offset[0], offset[0], offset[0] + xlen, offset[0] + xlen]])
    y = np.array([[offset[1], offset[1], offset[1], offset[1]],
                   [offset[1], offset[1], offset[1], offset[1]],
                   [offset[1] + ylen, offset[1] + ylen, offset[1] + ylen, offset[1] + ylen],
                   [offset[1] + ylen, offset[1] + ylen, offset[1] + ylen, offset[1] + ylen],
                   [offset[1], offset[1], offset[1], offset[1]]])
    z = np.array([[offset[2] + zlen, offset[2] + zlen, offset[2] + zlen, offset[2] + zlen],
                   [offset[2] + zlen, offset[2], offset[2], offset[2] + zlen],
                   [offset[2] + zlen, offset[2], offset[2], offset[2] + zlen],
                   [offset[2] + zlen, offset[2] + zlen, offset[2] + zlen, offset[2] + zlen],
                   [offset[2] + zlen, offset[2] + zlen, offset[2] + zlen, offset[2] + zlen]])
    return x, y, z

class task():
    def __init__(self):
        self.timeCost = 0;
        self.canOverlap = False;
        
class wareHouse():
    def __init__(self):
        self.length = 10;
        self.width = 10;
        self.height = 10;
        
    def aviliableAt(self, x, y, z):
        return False

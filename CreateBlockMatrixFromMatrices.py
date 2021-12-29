import numpy as np
from scipy.linalg import block_diag

def CreateBlockMatrix(ListOfMatrices):
    
    # Initialize BlockMatrix by first matrix from list
    BlockMatrix = ListOfMatrices[0]

    # Scipy package contains block_diag function which generates a block matrix from provided matrices
    for i in range(1,len(ListOfMatrices),1): BlockMatrix = block_diag(BlockMatrix,ListOfMatrices[i])

    return BlockMatrix

M1 = [[1,2,3],[4,5,6],[7,8,9]]
M2 = [[10,11,12],[13,14,15],[16,17,18]]
M3 = [[3,4],[5,5]]
M4 = [[1]]
M5 = [[100],[100]]

ListOfMatrices = [M1,M2,M3,M4,M5]

CreateBlockMatrix(ListOfMatrices)
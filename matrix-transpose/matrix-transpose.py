import numpy as np

def matrix_transpose(A):
    rows = len(A)
    cols = len(A[0])

    B = np.zeros((cols, rows))

    for i in range(rows):
        for j in range(cols):
            B[j, i] = A[i][j]

    return B
        

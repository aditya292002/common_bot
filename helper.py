import numpy as np
from cython_main import CalcRMSDRotationalMatrix

def rotation_matrix(a, b, weights=None):
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)

    if a.shape != b.shape:
        raise ValueError("'a' and 'b' must have same shape")

    if np.allclose(a, b) and weights is None:
        return np.eye(3, dtype=np.float64), 0.0

    N = b.shape[0]

    if weights is not None:
        weights = np.asarray(weights, dtype=np.float64) / np.mean(weights)

    rot = np.zeros(9, dtype=np.float64)

    rmsd = CalcRMSDRotationalMatrix(a, b, N, rot, weights)
    return rot.reshape(3, 3), rmsd

def run_rotation_matrix():
    # Define example data
    a = np.random.rand(500000, 3).astype(np.float64)
    b = np.random.rand(500000, 3).astype(np.float64)
    print(a)
    # Call the function
    rotation_matrix(a, b)

# Run the function
run_rotation_matrix()

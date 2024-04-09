import numpy as np
from cython_main import InnerProduct
from icecream import ic
from time import *

def main():
    sleep(1)
    # Declare constants with random values
    N = 10000000 # Number of elements
    coords1 = np.random.rand(N, 3)  # Random coordinates for array 1
    coords2 = np.random.rand(N, 3)  # Random coordinates for array 2
    weight = np.random.rand(N)  # Random weights

    # ic(coords1)
    # ic(coords2)
    # ic(weight)

    # Initialize array for result
    A = np.zeros(9)  # Flattened array

    # Call the Cython function
    result = InnerProduct(A, coords1, coords2, N, weight)

    # Print the result
    print("Weighted Inner Product:", result)

if __name__ == "__main__":
    main()

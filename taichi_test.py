import taichi as ti
import numpy as np
from icecream import ic

ti.init(arch=ti.cpu)  # Initialize Taichi

# Define constants
N = 10000000  # Number of elements

# Declare Taichi arrays
A = ti.field(ti.f32, shape=9)
coords1 = ti.Vector.field(3, dtype=ti.f32, shape=N)
coords2 = ti.Vector.field(3, dtype=ti.f32, shape=N)
weight = ti.field(ti.f32, shape=N)

# Fill coords1, coords2, and weight with random values
coords1.from_numpy(np.random.rand(N, 3).astype(np.float32))
coords2.from_numpy(np.random.rand(N, 3).astype(np.float32))
weight.from_numpy(np.random.rand(N).astype(np.float32))

# Declare variables G1 and G2
G1 = ti.field(ti.f32, shape=())
G2 = ti.field(ti.f32, shape=())

@ti.kernel
def inner_product() -> ti.f32:  # Annotate the return type
    G1[None] = ti.cast(0.0, ti.f32)
    G2[None] = ti.cast(0.0, ti.f32)

    # Initialize A
    for i in ti.static(range(9)):
        A[i] = 0.0

    if ti.static(weight != None):
        for i in range(N):
            x1 = weight[i] * coords1[i][0]
            y1 = weight[i] * coords1[i][1]
            z1 = weight[i] * coords1[i][2]

            G1[None] += x1 * coords1[i][0] + y1 * coords1[i][1] + z1 * coords1[i][2]

            x2 = coords2[i][0]
            y2 = coords2[i][1]
            z2 = coords2[i][2]

            G2[None] += weight[i] * (x2 * x2 + y2 * y2 + z2 * z2)

            A[0] += (x1 * x2)
            A[1] += (x1 * y2)
            A[2] += (x1 * z2)

            A[3] += (y1 * x2)
            A[4] += (y1 * y2)
            A[5] += (y1 * z2)

            A[6] += (z1 * x2)
            A[7] += (z1 * y2)
            A[8] += (z1 * z2)
    else:
        for i in range(N):
            x1 = coords1[i][0]
            y1 = coords1[i][1]
            z1 = coords1[i][2]

            G1[None] += (x1 * x1 + y1 * y1 + z1 * z1)

            x2 = coords2[i][0]
            y2 = coords2[i][1]
            z2 = coords2[i][2]

            G2[None] += (x2 * x2 + y2 * y2 + z2 * z2)

            A[0] += (x1 * x2)
            A[1] += (x1 * y2)
            A[2] += (x1 * z2)

            A[3] += (y1 * x2)
            A[4] += (y1 * y2)
            A[5] += (y1 * z2)

            A[6] += (z1 * x2)
            A[7] += (z1 * y2)
            A[8] += (z1 * z2)

    return (G1[None] + G2[None]) * 0.5

# Run the kernel
inner_product()

# Access and print the result
result = (G1[None] + G2[None]) * 0.5
print("Weighted Inner Product:", result)
# Copyright 2023 Luis Mantilla
#
# Licensed under the Apache License, Version 2.0.
# See <http://www.apache.org/licenses/LICENSE-2.0> for details.
"""A module to store common linear algebra functions."""
import numpy as np
import galois


__all__ = ["solve"]


def solve(A, b, check_solution=False):
    """
    Solve a linear system of equations Ax = b for x.
    """
    GF = galois.GF(2)
    A = GF(A.astype(np.uint8))
    b = GF(b.astype(np.uint8))

    rows, cols = A.shape
    augmented_matrix = np.hstack((A, b.reshape(-1, 1)))

    row = 0
    for col in range(cols):
        # Find pivot in current column
        for pivot_row in range(row, rows):
            if augmented_matrix[pivot_row, col]:
                break
        else:
            continue

        # Swap rows if needed
        if pivot_row != row:
            augmented_matrix[[row, pivot_row]] = augmented_matrix[[pivot_row, row]]

        # Zero out below pivot
        for i in range(row + 1, rows):
            if augmented_matrix[i, col]:
                augmented_matrix[i] ^= augmented_matrix[row]

        row += 1

        if row >= rows:
            break

    # Back-substitution
    x = np.zeros(cols, dtype=int)
    for row in range(min(rows, cols) - 1, -1, -1):
        col = np.argmax(augmented_matrix[row, :cols])
        x[col] = augmented_matrix[row, -1] ^ np.sum(
            augmented_matrix[row, col + 1 : cols] * x[col + 1 : cols]
        )

    x = GF(x)
    if check_solution:
        x = x.reshape(-1, 1)
        if not np.linalg.norm(A @ x - b) < 1e-9:
            raise ValueError("Solution not found")

    return x

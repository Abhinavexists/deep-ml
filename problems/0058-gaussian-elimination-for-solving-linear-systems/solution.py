import numpy as np

def gaussian_elimination(A, b):
    n = len(A)
    x = np.zeros(n)

    # Forward elimination
    for k in range(n - 1):

        # Find largest pivot in current column
        pivot = k + np.argmax(np.abs(A[k:, k]))

        # Swap rows
        if pivot != k:
            A[[k, pivot]] = A[[pivot, k]]
            b[[k, pivot]] = b[[pivot, k]]

        # Eliminate entries below pivot
        for i in range(k + 1, n):
            m = A[i][k] / A[k][k]

            A[i, k:] -= m * A[k, k:]
            b[i] -= m * b[k]

    # Back substitution
    for k in range(n - 1, -1, -1):
        x[k] = (
            b[k] - np.dot(A[k, k + 1:], x[k + 1:])
        ) / A[k, k]

    return x
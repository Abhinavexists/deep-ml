import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute the rank of a matrix.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero
    
    Returns:
        The rank of the matrix (integer)
    """
    # Your code here
    # return np.linalg.matrix_rank(A)

    A = [row[:] for row in A]

    rows = len(A)
    cols = len(A[0])
    rank = 0

    for col in range(cols):
        pivot = None

        for row in range(rank, rows):
            if A[row][col] != 0:
                pivot = row
                break
        
        if pivot is None:
            continue

        A[rank], A[pivot] = A[pivot], A[rank]

        for row in range(rank + 1, rows):
            if A[row][col] != 0:
                factor = A[row][col] / A[rank][col]

                for j in range(col, cols):
                    A[row][j] -= factor * A[rank][j]

        rank += 1

        if rank == rows:
            break

    return rank
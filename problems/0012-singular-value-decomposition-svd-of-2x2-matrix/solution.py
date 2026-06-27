import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    
    Args:
        A: A 2x2 numpy array
    
    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
        - U: 2x2 orthogonal matrix
        - S: length-2 array of singular values
        - Vt: 2x2 orthogonal matrix (transpose of V)
    """
    # Your code here
    #     [
    #     [
    #         A[0,0]**2 + A[1,0]**2,
    #         A[0,0]*A[0,1] + A[1,0]*A[1,1]
    #     ],
    #     [
    #         A[0,0]*A[0,1] + A[1,0]*A[1,1],
    #         A[0,1]**2 + A[1,1]**2
    #     ]
    # ]
    B = A.T@A

    if B[0,0] == B[1,1]:
        theta = np.pi/4
    else:
        theta = 0.5 * np.arctan2(2*B[0,1], B[0,0] - B[1,1])

    R = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

    D = R.T @ B @ R

    lambda1 = D[0,0]
    lambda2 = D[1,1]

    sigma1 = np.sqrt(max(lambda1, 0))
    sigma2 = np.sqrt(max(lambda2, 0))

    sigma_inv = np.diag([1/sigma1 if sigma1 > 1e-12 else 0, 1/sigma2 if sigma2 > 1e-12 else 0])

    V = R
    U = A @ V @ sigma_inv
    Vt = V.T
    S = np.array([sigma1, sigma2])
    
    return U, S, Vt
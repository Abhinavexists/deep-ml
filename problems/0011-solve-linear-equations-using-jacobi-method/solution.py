import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	x = np.zeros(len(b))

	for i in range(n):
		x_new = np.empty_like(x)

		for i in range(len(b)):
			sigma = np.dot(A[i], x) - (A[i, i] * x[i])
			x_new[i] = np.round((b[i] - sigma)/A[i, i], 4)
		x = x_new
	return x.tolist()
import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	n = len(A[0])
	a = np.array(A)
	s = np.array(S)
	t = np.array(T)
	t_inverse = np.linalg.inv(t)
	i = np.identity(n)

	if np.linalg.det(t) == 0 or np.linalg.det(s) == 0:
		return -1

	transformed_matrix = t_inverse @ a @ s
	return transformed_matrix
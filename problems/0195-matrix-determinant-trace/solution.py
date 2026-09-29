def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	# Your code here
	n = len(matrix)

	def traces(n , matrix):
		tr = 0
		for i in range(n):
			for j in range(n):
				if i == j:
					tr += matrix[i][j]
		return tr

	def determinant(n, matrix):

		if n == 1:
			return matrix[0][0]

		det = 0

		for j in range(n):
			minor = [
				[matrix[i][k] for k in range(n) if k != j]
				for i in range(1, n)
			]
			sign = (-1) ** j
			det += sign*matrix[0][j]*determinant(n-1, minor)
		return det

	return determinant(n, matrix), traces(n, matrix)
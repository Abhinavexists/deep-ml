def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	scalar_matrix = []
	for row in matrix:
		scalar_row = []
		for i in row:
			i *= scalar
			scalar_row.append(i)
		scalar_matrix.append(scalar_row)

	return scalar_matrix
	
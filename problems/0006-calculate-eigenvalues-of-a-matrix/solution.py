def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	determinant = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
	trace_sum = 0
	for i in range(len(matrix)):
		trace_sum += matrix[i][i]
	a = 1
	c = determinant
	d = (trace_sum**2) - (4*a*c)
	lambda_1 = -(-trace_sum - d**(1/2))/(2*a)
	lambda_2 = -(-trace_sum + d**(1/2))/(2*a)

	eigenvalues = [lambda_1, lambda_2]

	return eigenvalues
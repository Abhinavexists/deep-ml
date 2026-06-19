def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode == "row":
		for row in matrix:
			means.append(sum(row)/len(row))
		return means
	else:
		for col in range(len(matrix[0])):
			col_sum = 0
			for row in range(len(matrix)):
				col_sum += matrix[row][col]
			mean = col_sum/len(matrix)
			means.append(mean)

	return means
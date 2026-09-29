import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	rows = len(data)
	cols = len(data[0])

	means = []
	stds = []
	mins = []
	maxs = []

	standardized_data = []
	normalized_data = []

	for i in range(cols):
		columns = [data[j][i] for j in range(rows)]

		mean = sum(columns)/rows
		var = sum((x-mean)**2 for x in columns)/rows
		std = var ** 0.5
		minimum = min(columns)
		maximum = max(columns)

		means.append(mean)
		stds.append(std)
		mins.append(minimum)
		maxs.append(maximum)

	for i in range(rows):
		std_row = []
		nor_row = []
		for j in range(cols):
			std_row.append(
				(data[i][j] - means[j])/stds[j]
			)
			nor_row.append(
				(data[i][j] - mins[j])/ (maxs[j] - mins[j])
			)
		standardized_data.append(std_row)
		normalized_data.append(nor_row)


	return standardized_data, normalized_data
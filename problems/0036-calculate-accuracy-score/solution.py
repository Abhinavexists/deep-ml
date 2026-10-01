import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	n = len(y_pred)
	corr = 0

	for i in range(n):
		if y_true[i] == y_pred[i]:
			corr += 1
		i = i+1

	return corr/n
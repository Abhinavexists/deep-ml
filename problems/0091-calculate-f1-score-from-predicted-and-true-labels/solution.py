def calculate_f1_score(y_true, y_pred):
	"""
	Calculate the F1 score based on true and predicted labels.

	Args:
		y_true (list): True labels (ground truth).
		y_pred (list): Predicted labels.

	Returns:
		float: The F1 score rounded to three decimal places.
	"""
	# Your code here
	tp = 0
	fp = 0
	fn = 0

	for i in range(len(y_true)):
		if y_true[i] == y_pred[i] and y_true[i] == 1:
			tp += 1
		elif y_true[i] == y_pred[i] and y_true[i] == 0:
			fn += 1
		else:
			if y_true[i] != y_pred[i] and y_true[i] == 0:
				fp += 1
			else:
				pass
	if tp != 0:
		precision = tp/(tp + fp)
		recall = tp/(tp + fn) 

		f1 = 2*((precision * recall)/(precision + recall))
		return round(f1,3)
	else:
		return 0
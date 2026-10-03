
import numpy as np

def rmse(y_true, y_pred):
	y_true = np.array(y_true)
	y_pred = np.array(y_pred)

	return np.round(np.sqrt(np.mean((y_true - y_pred) ** 2)), 3)

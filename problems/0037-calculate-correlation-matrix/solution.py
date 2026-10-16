import numpy as np


def calculate_correlation_matrix(X, Y=None):
    if Y is None:
        # rowvar is false because every column contains variables and row contains observations here
        return np.corrcoef(X, rowvar=False)

    n = X.shape[1]
    return np.corrcoef(np.column_stack((X, Y)), rowvar=False)[:n, n:]
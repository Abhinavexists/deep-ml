import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	return np.sum(np.dot(v1, v2), axis=0)/(np.sqrt((np.sum(np.dot(v1, v1), axis=0)))*(np.sqrt(np.sum(np.dot(v2, v2), axis=0))))
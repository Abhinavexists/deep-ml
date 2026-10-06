
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	proj = []

	for i in range(len(v)):
		proj.append(((v[i]*L[i])/(L[i]*L[i]))*L[i] if L[i] != 0 else 0)

	return proj
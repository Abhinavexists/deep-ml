def selu(x: float) -> float:
	"""
	Implements the SELU (Scaled Exponential Linear Unit) activation function.

	Args:
		x: Input value

	Returns:
		SELU activation value
	"""
	alpha = 1.6732632423543772
	scale = 1.0507009873554804
	e = 2.718281828459045

	if x > 0:
		return scale*x
	else:
		return scale * alpha * (e**x - 1)
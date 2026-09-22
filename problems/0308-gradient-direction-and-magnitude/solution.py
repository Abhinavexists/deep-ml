import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	l2 = np.sqrt(np.sum(np.power(gradient, 2)))

	if l2 == 0:
		return {
        'magnitude': 0.0,
        'direction': np.zeros(len(gradient)),
        'descent_direction': np.zeros(len(gradient))
    }

	direction = [x/l2 for x in gradient]
	descent_direction = [x/-1 for x in direction]

	return {
		'magnitude': l2,
		'direction': direction,
		'descent_direction': descent_direction
	}
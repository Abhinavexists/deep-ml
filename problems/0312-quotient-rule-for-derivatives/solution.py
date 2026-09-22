import numpy as np


def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.

    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative

    Returns:
        The derivative value f'(x)
    """
    # Your code here
    poly = np.polynomial.polynomial

    # issue was numpy api carries polynomial in decreasing order and need to bring back in asc/increasing order
    g_asc = g_coeffs[::-1] # need to bring to asc
    h_asc = h_coeffs[::-1]

    dg = poly.polyder(g_asc)
    dh = poly.polyder(h_asc)

    g_x = poly.polyval(x, g_asc)
    h_x = poly.polyval(x, h_asc)
    dg_x = poly.polyval(x, dg)
    dh_x = poly.polyval(x, dh)  

    if h_x == 0:
        raise ZeroDivisionError(
            f"The denominator h(x) evaluates to zero at x = {x}."
        )

    return (dg_x * h_x - g_x * dh_x) / (h_x) ** 2

def divide_numbers(a, b):
    """
    Divide two numbers.

    Parameters
    ----------
    a : float
        The dividend.
    b : float
        The divisor.

    Returns
    -------
    float
        The quotient of the division.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


def power(a, b):
    ' ' 'Returns arg1 raised to power arg2.' ' '
  
    return a**b
 


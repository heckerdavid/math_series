def fibonacci(n):
    """
    accepts an int, returns the value of (int)th fibonacci number
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """
    accepts an int, returns the value of (int)th lucas number
    """
    if n == 1:
        return 1
    elif n == 0:
        return 2
    return lucas(n - 1) + lucas(n - 2)

def sum_series(n, a=0, b=1):
    """ Accepts an int (a), returns the (a)th value from the sum series. optional params b and c modify the initial two values, default initial values are 0 & 1"""
    if n == 0:
       return a
    elif n == 1:
        return b
    return sum_series(n - 1, a, b) + sum_series(n - 2, a, b)
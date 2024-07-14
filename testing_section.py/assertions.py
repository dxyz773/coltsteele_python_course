def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive"
    return x + y


# print(add_positive_numbers(1, 1))
# print(add_positive_numbers(1, -1))


def add(a, b):
    """
    >>> add(2,3)
    5
    >>> add(100,200)
    300
    """
    return a + b


def double(values):
    """double the values in a list
    >>> double([1,2,3,4])
    [2,4,6,8]

    >>> double([])
    []

    >>> double([-1,-2,-3,-4])
    [-2,-4,-6,-8]

    >>> double(['a','b','c'])
    ['aa','bb','cc']

    """

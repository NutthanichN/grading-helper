"""
Helper module for testing random
"""


def _randint_wrapper(_):
    index = -1

    def func(a: int, b: int) -> int:
        nonlocal index
        index += 1
        return range(a, b + 1)[index % len(range(a, b + 1))]

    return func


@_randint_wrapper
def randint():
    """ Return int in the range [a, b], cycling from a to b """
    # Use decorator to make IDE recognize randint as a function, not a variable
    pass


def _random_wrapper(_):
    index = -1
    subdivision = 100

    def func() -> float:
        nonlocal index
        index += 1
        return index / subdivision % 1

    return func


@_random_wrapper
def random():
    """ Return number in the range [0, 1) incrementing in subdivisions """
    pass

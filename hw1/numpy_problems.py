import numpy as np


##########
# PART 3 #
##########
# TASK: Implement the below functions. Some basic tests for
#  each function are included in test/test_numpy.py. Feel free to add more!


def find_missing(n: int, arr: np.ndarray) -> np.ndarray:
    """Given a positive integer `n` and a sorted array `arr` containing a subset
    of the range [0, n), return a sorted array containing the missing integers from
    the range [0, n).

    You can assume that all inputs to the function are valid.

    find_missing(6, [0, 2, 5])
    [1, 3, 4]
    """
    # BEGIN_YOUR_CODE
    return np.setdiff1d(np.arange(n), arr, assume_unique=True)
    # END_YOUR_CODE


def skyline(heights: np.ndarray) -> int:
    """Given an array `heights` that encodes the heights of buildings in a city skyline, return
    the total number of unique buildings that are visible when standing to the left of the skyline.
    A given building is visible if it is taller than all buildings to its left.

    You can assume that all elements in `heights` are positive.

    skyline([5, 5, 2, 10, 3, 15])
    3
    """
    # BEGIN_YOUR_CODE
    maxes = np.maximum.accumulate(np.pad(heights, (1, 0)))
    return np.sum(heights > maxes[:-1])
    # END_YOUR_CODE


def matched(parentheses: np.ndarray) -> bool:
    """Given an array `parentheses` where every element is '(' or ')', return whether it is a
    balanced set of parentheses. Concretely, this means that each opening parenthesis has a closing
    parenthesis, and for each pair of opening and closing parentheses, the opening parenthesis
    exists to the left of the closing parenthesis.

    matched(['(', ')'])
    True

    matched(['(', ')', ')'])
    False
    """
    # BEGIN_YOUR_CODE
    deltas = np.zeros_like(parentheses, dtype=int)
    deltas[parentheses == '('] = 1
    deltas[parentheses == ')'] = -1
    tally = np.cumsum(deltas)
    return (tally >= 0).all() and tally[-1] == 0
    # END_YOUR_CODE

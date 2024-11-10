from functools import reduce

from sympy import expand, lambdify, symbols

from utils import open_file

# Slow solution (takes about a minute) but it made part 2 very easy (just shift the x sequence forward by 1).
# This page explains well how to get the Lagrange polynomial: https://www.geeksforgeeks.org/lagrange-interpolation-formula/
# Thanks to this StackOverflow answer for the implementation: https://stackoverflow.com/a/56827866/6453088
# A better solution making use of Numpy is here: https://www.reddit.com/r/adventofcode/comments/18e5ytd/comment/kclqhga/?utm_source=share&utm_medium=web2x&context=3


def solution():
    values = list(
        map(lambda line: list(map(int, line.split())), open_file("9").split("\n"))
    )
    solution_1 = __solution_1(values)
    solution_2 = __solution_2(values)
    return (solution_1, solution_2)


def __solution_1(sequences: list[list[int]]):
    def get_next_value_in_sequence(result: int, sequence: list[int]):
        fn = get_lagrange_polynomial_fn(sequence)
        return result + fn(len(sequence))

    return int(reduce(get_next_value_in_sequence, sequences, 0))


def __solution_2(sequences: list[list[int]]):
    def get_previous_value_in_sequence(result: int, sequence: list[int]):
        fn = get_lagrange_polynomial_fn(sequence, range(1, len(sequence) + 1))
        return result + fn(0)

    return int(reduce(get_previous_value_in_sequence, sequences, 0))


def get_lagrange_polynomial_fn(y_sequence: list[int], x_sequence=None):
    if x_sequence is None:
        x_sequence = range(0, len(y_sequence))

    x = symbols("x")
    zero_polynomial = x - x
    one_polynomial = zero_polynomial + 1

    result = zero_polynomial
    for j, (x_j, y_j) in enumerate(zip(x_sequence, y_sequence)):
        polynomial_for_j = one_polynomial
        for m, x_m in enumerate(x_sequence):
            if m != j:
                polynomial_for_j *= (x - x_m) / (x_j - x_m)
        result += y_j * polynomial_for_j
    expression = expand(result)
    return lambdify([x], expression)

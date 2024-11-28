from utils import open_file


def solution():
    line = open_file("15")
    solution_1 = __solution_1(line)
    solution_2 = __solution_2(line)
    return (solution_1, solution_2)


def __solution_1(line: str) -> int:
    result = 0
    sub_total = 0
    for char in line:
        if char == ",":
            result += sub_total
            sub_total = 0
            continue

        sub_total += ord(char)
        sub_total *= 17
        sub_total = sub_total % 256
    return result + sub_total


def __solution_2(line: str):
    return None


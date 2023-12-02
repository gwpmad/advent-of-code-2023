from utils import open_file


def __solution_1(values: list[str]) -> int:
    numbers = map(__get_number_from_line, values)
    return sum(numbers)


def __solution_2(values: list[str]) -> int:
    numbers = map(__get_number_from_line_incl_text, values)
    return sum(numbers)


def __get_number_from_line(line: str) -> int:
    chars: list[str] = list(line)
    numbers = [x for x in chars if x.isdigit()]
    return int(f"{numbers[0]}{numbers[-1]}")


def __get_number_from_line_incl_text(line: str) -> int:
    substr_from_beginning = ""
    substr_from_end = ""
    first_digit = None
    last_digit = None

    for char in line:
        if char.isdigit():
            first_digit = int(char)
            break
        substr_from_beginning = f"{substr_from_beginning}{char}"
        first_digit = get_matching_digit_at_end_of_string(substr_from_beginning)
        if first_digit is not None:
            break

    for char in line[::-1]:
        if char.isdigit():
            last_digit = int(char)
            break
        substr_from_end = f"{char}{substr_from_end}"
        last_digit = get_matching_digit_at_beginning_of_string(substr_from_end)
        if last_digit is not None:
            break

    return int(f"{first_digit}{last_digit}")


def solution():
    values = open_file("1").split("\n")
    solution_1 = __solution_1(values)
    solution_2 = __solution_2(values)
    return (solution_1, solution_2)


__text_to_digit = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

__text_digits = __text_to_digit.keys()


def get_matching_digit_at_end_of_string(string: str) -> int | None:
    for text_digit in __text_digits:
        if string.endswith(text_digit):
            return __text_to_digit[text_digit]
    return None


def get_matching_digit_at_beginning_of_string(string: str) -> int | None:
    for text_digit in __text_digits:
        if string.startswith(text_digit):
            return __text_to_digit[text_digit]
    return None

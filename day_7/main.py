from functools import cmp_to_key, reduce

from utils import open_file


def solution():
    values = open_file("7").split("\n")
    solution_1 = __solution_1(values)
    solution_2 = __solution_2(values)
    return (solution_1, solution_2)


card_strengths = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}


def parse_hands(value: str, part_2: bool = False):
    parts = value.split()

    chars = {}
    for char in parts[0]:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    if part_2 and "J" in chars and len(chars) > 1:
        j_value = chars["J"]
        chars = {key: chars[key] for key in chars if key != "J"}
        top_key = max(chars, key=lambda key: chars[key])
        chars[top_key] += j_value

    chars_len = len(chars)
    strength = 7 if chars_len == 1 else 1
    if chars_len == 2:
        strength = 6 if 4 in list(chars.values()) else 5
    elif chars_len == 3:
        strength = 4 if 3 in list(chars.values()) else 3
    elif chars_len == 4:
        strength = 2
    return {"strength": strength, "bid": int(parts[1]), "hand": parts[0]}


def compare_hands(a, b) -> int:
    strength_difference = a["strength"] - b["strength"]
    if strength_difference == 0:
        for i in range(0, 5):
            strength_difference = (
                card_strengths[a["hand"][i]] - card_strengths[b["hand"][i]]
            )
            if strength_difference != 0:
                break
    return strength_difference


def get_total_winnings(hands):
    hands.sort(key=cmp_to_key(compare_hands))
    return reduce(
        lambda acc, iv: acc + ((iv[0] + 1) * iv[1]["bid"]), enumerate(hands), 0
    )


def __solution_1(values: list[str]):
    hands = list(map(parse_hands, values))
    return get_total_winnings(hands)


def __solution_2(values: list[str]):
    card_strengths["J"] = 0
    hands = list(map(lambda value: parse_hands(value, part_2=True), values))
    return get_total_winnings(hands)

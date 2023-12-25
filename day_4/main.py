import re

from utils import open_file


def solution():
    values = open_file("4").split("\n")
    solution_1 = __solution_1(values)
    solution_2 = __solution_2(values)
    return (solution_1, solution_2)


def get_number_of_winning_tickets(ticket: str) -> int:
    halves = list(map(lambda x: re.findall(r"(\d+)(?![\d:])", x), ticket.split("|")))
    return len(list(set(halves[0]) & set(halves[1])))


def __solution_1(values: list[str]):
    answer = 0
    for value in values:
        winning_tickets = get_number_of_winning_tickets(value)
        if winning_tickets > 0:
            answer += 2 ** (winning_tickets - 1)
    return answer


def __solution_2(values: list[str]):
    queue = [{"win_count": get_number_of_winning_tickets(x), "n": 1} for x in values]

    for idx, current in enumerate(queue):
        current = queue[idx]
        for _ in range(current["n"]):
            for i in range(idx + 1, idx + 1 + current["win_count"]):
                queue[i]["n"] += 1

    return sum(card["n"] for card in queue)

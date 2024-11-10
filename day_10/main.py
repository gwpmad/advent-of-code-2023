from utils import open_file


def solution():
    values = open_file("10")
    solution_1 = __solution_1(values)
    solution_2 = __solution_2(values)
    return (solution_1, solution_2)


class ListNode:
    def __init__(self, next: "ListNode | None" = None):
        self.next = next


class LinkedList:
    def __init__(self, head: ListNode):
        self.head = head

    def size(self):
        node = self.head
        count = 0
        while True:
            node = node.next
            count += 1
            if node is None or node == self.head:
                break

        return count

    def get_last(self):
        last = self.head
        while last.next is not None:
            last = last.next
        return last

    def push(self):
        last = self.get_last()
        last.next = ListNode()


def __solution_1(input: str):
    side_length = input.find("\n") + 1

    pipes = get_pipes(side_length)
    s_idx = input.find("S")
    list = LinkedList(ListNode())
    previous_idx = s_idx
    current_idx = find_first_pipe(input, previous_idx, pipes)

    while current_idx != s_idx:
        list.push()
        for difference, possibles in pipes:
            if (
                input[current_idx] in possibles
                and current_idx + difference != previous_idx
            ):
                previous_idx = current_idx
                current_idx = current_idx + difference
                break
    return list.size() / 2


def get_pipes(side_length: int):
    return [
        (-1, {"-", "J", "7"}),
        (side_length, {"|", "7", "F"}),
        (1, {"-", "L", "F"}),
        (-side_length, {"|", "L", "J"}),
    ]


def find_first_pipe(input: str, start_idx: int, pipes: list) -> int:
    for difference, possibles in pipes:
        if input[start_idx - difference] in possibles:
            return start_idx - difference
    raise Exception("No pipe found")


def __solution_2(input: str):
    return None


# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.

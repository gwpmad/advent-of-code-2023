from utils import open_file


def solution():
    values = open_file("13").translate(str.maketrans({'.': '0', '#': '1'})).split("\n\n")
    solution_1 = __solution_1(values)
    solution_2 = __solution_2(values)
    return (solution_1, solution_2)

def __solution_1(blocks: list[str]) -> int:
    final_result = 0
    for block in blocks:
        ints_array = __get_array_of_ints(block.split('\n'))

        block_result = __get_reflect_begin(ints_array)
        if block_result > 0:
            final_result += block_result * 100
            continue

        ints_array = __get_array_of_ints(__get_transposed_block(block))
        block_result = __get_reflect_begin(ints_array)
        final_result += block_result
    
    return final_result

def __solution_2(blocks: list[str]):
    final_result = 0
    for block in blocks:
        ints_array = __get_array_of_ints(block.split('\n'))

        block_result = __get_reflect_begin_with_smudge(ints_array)
        if block_result > 0:
            final_result += block_result * 100
            continue

        ints_array = __get_array_of_ints(__get_transposed_block(block))
        block_result = __get_reflect_begin_with_smudge(ints_array)
        final_result += block_result

    return final_result

class Base2And10Representation:
    def __init__(self, base_2: str, base_10: int):
        self.base_2 = base_2
        self.base_10 = base_10

    base_2: str
    base_10: int

def __get_reflect_begin_with_smudge(ints_array: list[Base2And10Representation]):
    number_of_ints = len(ints_array)
    for idx in range(1, number_of_ints):
        extent = idx if number_of_ints - idx > idx else number_of_ints - idx
        smudge_handled = False

        for i in range(1, extent+1):
            comparee_1 = ints_array[idx + i - 1]
            comparee_2 = ints_array[idx - i]
            reflected = comparee_1.base_10 == comparee_2.base_10
            if not reflected:
                if not smudge_handled:
                    if __one_char_difference_only(comparee_1.base_2, comparee_2.base_2):
                        smudge_handled = True
                    else:
                        break
                else:
                    break
            if i == extent and smudge_handled:
                return idx
    return 0


def __get_reflect_begin(ints_array: list[Base2And10Representation]):
    number_of_ints = len(ints_array)
    for idx in range(1, number_of_ints):
        extent = idx if number_of_ints - idx > idx else number_of_ints - idx
        for i in range(1, extent+1):
            reflected = ints_array[idx + i - 1].base_10 == ints_array[idx - i].base_10
            if not reflected:
                break
            if i == extent:
                return idx
    return 0

def __one_char_difference_only(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False

    difference = 0
    for idx in range(len(str1)):
        if str1[idx] != str2[idx]:
            difference += 1
            if difference > 1:
                break

    return difference == 1

def __get_array_of_ints(lines: list[str]) -> list[Base2And10Representation]:
    return [Base2And10Representation(base_10=int(line,base=2), base_2=line) for line in lines]

def __get_transposed_block(block: str) -> list[str]:
    array = [list(line) for line in block.split('\n')]
    return [''.join(split_line) for split_line in [*zip(*array)]]


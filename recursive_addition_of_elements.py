from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    """
    Code returns a recursive addition of elements (even the nested ones) 
    """
    total = 0

    for j in range(len(sequence)):
        if type(sequence[j]) == list:
            total += seq_sum(sequence[j])
        elif type(sequence[j]) == tuple:
            total += seq_sum(sequence[j])
        else:
            total += sequence[j]
    return total


if __name__ == "__main__":
    assert seq_sum([1, 2, 3, [4, 5, (6, 7)]])

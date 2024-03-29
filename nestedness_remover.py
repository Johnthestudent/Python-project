from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    """
    Code returns a sequence, that has no nestedness   
    """
    n = len(sequence)
    if n == 0:
        return sequence
    elif n == 1:
        item = sequence[0]
        try:
            return linear_seq(list(item))
        except TypeError:
            return [item]
    else:
        k = n // 2
        return linear_seq(sequence[:k]) + linear_seq(sequence[k:])


if __name__ == "__main__":
    assert linear_seq([1, 2, 3, [4, 5, (6, 7)]])

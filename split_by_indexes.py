from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:
    """
    Code returns string split by the given indexes   
    """
    parts = [s[i:j] for i, j in zip([0] + indexes, indexes + [None])]
    if '' in parts:
        parts.pop()
    print(parts)
    return parts
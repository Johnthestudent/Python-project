from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    # Code returns a tuple, that has the pairs of elements out of the list
    if(len(lst) == 1):
        print([])
        return []
    elif(len(lst) > 1):
        my_list = []
        for i, j in zip(lst, lst[1:]):
            my_list.append((i, j))
        print(my_list)
        return my_list

if __name__ == "__main__":
    assert get_pairs([1, 2, 3, 4])
    assert get_pairs(['a', 'b', 'c', 'd'])

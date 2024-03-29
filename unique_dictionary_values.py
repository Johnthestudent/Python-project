from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    """
    Code returns unique values out of the dictionary 
    """
    unique_values = set(val for dic in lst for val in dic.values())
    print(unique_values)
    return unique_values


if __name__ == "__main__":
    assert check([{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
                  {"VIII": "S007"}])

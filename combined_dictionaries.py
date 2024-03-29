from typing import List, Dict

#Code returns combined dictionaries
def combine_dicts(*args:List[Dict[str, int]]) -> Dict[str, int]:
    keys = set()
    for arg in args:
        keys = keys.union(arg.keys())
    new_dictionary = {k: sum(arg.get(k, 0) for arg in args) for k in keys}
    print(new_dictionary)
    return new_dictionary

if __name__ == "__main__":
    assert combine_dicts({'a': 100, 'b': 200}, {'a': 200, 'c': 300}, {'b': 100, 'd': 300})
#Code returns intersect and union of sets, tuples and lists
def union(*args) -> set:
    result_set = set()
    for i in args:
        if type(i) != set:
            i = set(i)
        result_set = i.union(*args)
    print(result_set)
    return result_set

def intersect(*args) -> set:
    result_set = set()
    for i in args:
        if type(i) != set:
            i = set(i)
        result_set = i.intersection(*args)
    print(result_set)
    return result_set

if __name__ == "__main__":
    assert union({'A', 'B', 'C'}, ['A', 'B', 'D'], ('E', 'F'))
    assert intersect({'A', 'B', 'C'}, ['A', 'B', 'D'], ('E', 'F', 'A'))

from typing import List, Tuple

def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    # Code shows a list of sorted unique elements
    output = []
    for x in str_list:
        if x not in output:
            output.append(x)
    final_result = sorted(output)
    print(final_result)
    return final_result

if __name__ == "__main__":
    assert sort_unique_elements(["xyz" ,"abc", "cde", "abc"])

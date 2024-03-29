from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    # Code returns a fizzbuzz list
    result_list = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result_list.append("FizzBuzz")
        elif i % 3 == 0:
            result_list.append("Fizz")
        elif i % 5 == 0:
            result_list.append("Buzz")
        else:
            result_list.append(i)
    print(result_list)
    return result_list

if __name__ == "__main__":
    assert get_fizzbuzz_list(3)
    assert get_fizzbuzz_list(5)
    assert get_fizzbuzz_list(15)

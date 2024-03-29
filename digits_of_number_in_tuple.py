from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    # Code returns digits of a number
    my_digits = [int(digit) for digit in str(num)]
    final_tuple = tuple(my_digits)
    print(final_tuple)
    return final_tuple

if __name__ == "__main__":
    assert get_tuple((12345))
    assert get_tuple((1234567890))
from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    """
    Code returns a dictionary, where the key is a number and the value is the square of that number  
    """
    dictionary_of_squares = dict()
    for i in range(1, num + 1):
        dictionary_of_squares[i] = i ** 2
    print(dictionary_of_squares)
    return dictionary_of_squares

if __name__ == "__main__":
    assert generate_squares(5)

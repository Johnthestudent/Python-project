from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values
    # Code overwrites the behavior of the __add__ magic method
    def __add__(self, other):
        result_string = []
        list_string = map(str, self.values)
        converted_string = list(list_string)
        for i in range(0, len(self.values)):
            result_string.append(str(converted_string[i] + " " + other))
        print(result_string)
        return result_string


from typing import Union

NumType = Union[int, float]

def some_expression_with_rounding(a: NumType, b: NumType) -> NumType:
  result = None
  discriminant = (12 * a + 25 * b) / (1 + a**(2**b))	#the calculated formula
  result = round(discriminant, 2)
  print(result)
  return result

if __name__ == "__main__":
    assert some_expression_with_rounding(1, 6)
    assert some_expression_with_rounding(1, 4)
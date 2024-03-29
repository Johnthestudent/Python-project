from typing import Union


def divide(str_with_ints: str) -> Union[float, str]:
    """
    Returns the result of dividing two numbers or an error message.
    :arg
        str_with_ints: str, ex. "4 2";
    :return
        result of dividing: float, ex. 2.0 (4 / 2 = 2.0);
        error response in "Error code: {error message}: str;
    """
    #Usage example at the last lines of the program
    try:
        first_number = int(str_with_ints.split(" ")[0])
        second_number = int(str_with_ints.split(" ")[-1])
        result_number = first_number / second_number
    except ZeroDivisionError as e:
        print(f'Error code: {e}')
    except ValueError as g:
        print(f'Error code: {g}')
    else:
        result_number = first_number / second_number
        print(result_number)
        return result_number

divide("4       2")
divide("4 0")
divide("* 1")
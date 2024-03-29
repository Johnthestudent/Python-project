def get_fractions(a_b: str, c_b: str) -> str:
    """
    This code makes fraction addition from numbers given in a string 
    """
    if(a_b[-1:] == c_b[-1:]):
        a_to_number = int(a_b[0:1])
        b_to_number = int(c_b[0:1])
        addition_result = a_to_number + b_to_number
        final_result = a_b + " + " + c_b + " = " + str(addition_result) + "/" + a_b.split("/")[-1]
        print(final_result)
        return final_result

if __name__ == "__main__":
    assert get_fractions('1/33', '2/33')
    assert get_fractions('1/5', '4/5')
    assert get_fractions('1/120', '4/120')

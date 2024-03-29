def get_longest_word( s: str) -> str:
    """
    Code returns the longest word of the input 
    """
    if "\n" not in s.split(" ") or "\t" not in s.split(" ") or " " not in s.split(" "):
        longest_one = max(s.split(" "), key=len)
    return longest_one

if __name__ == "__main__":
    assert get_longest_word('Hello Mr. Programmer! John')
    assert get_longest_word('abba baba bab')
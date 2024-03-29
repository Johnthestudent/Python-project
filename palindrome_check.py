def check_str(s: str):
    """
    Code checks whether the input string is a palindrome or not
    """
    palindrome_check = False
    if (s[0].lower() == s[len(s) - 1].lower() and s[1].lower() == s[len(s) - 2].lower()):
        palindrome_check = True
        print(palindrome_check)
    elif (s[0].lower() != s[len(s) - 1].lower() and s[1].lower() != s[len(s) - 2].lower()):
        palindrome_check = False
        print(palindrome_check)
    return palindrome_check

if __name__ == "__main__":
    assert check_str("Rise to vote, sir")
    assert check_str("Race car")

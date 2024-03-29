def replacer(s: str) -> str:
    """
    Code replaces " and ' quotes
    """
    renewed_string = ''
    replace_this = "\'"
    to_this = "\""
    for i in range(0, len(s)):
        if s[i] == replace_this:
            renewed_string += to_this
        elif s[i] == to_this:
            renewed_string += replace_this
        else:
            renewed_string += s[i]
    print(renewed_string)
    return renewed_string


if __name__ == "__main__":
    assert replacer("""Hello Mr.'' Programmer ""John""")
    assert replacer("""abba ""baba ''bab""")

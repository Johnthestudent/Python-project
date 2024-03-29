from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    # Code returns the number of occurences of a character
    character_occurences = dict()
    for i in s.lower():
        if i in character_occurences:
            character_occurences[i] += 1
        else:
            character_occurences[i] = 1
    print(character_occurences)
    return character_occurences

if __name__ == "__main__":
    assert get_dict('abcCBA ,g')
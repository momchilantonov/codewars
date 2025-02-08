import re


def solution(s):
    """
    Complete the solution so that it splits the string into
    pairs of two characters. If the string contains an odd 
    number of characters then it should replace the missing 
    second character of the final pair with an underscore ('_').
    """

    if not len(s) % 2 == 0:
        s += "_"

    pattern = r"(?P<search>[a-z_]{2})"
    matches = re.finditer(pattern, s)
    pairs = [el.group() for el in matches]

    return pairs


# TESTS
solution("abcdef")  # ["ab", "cd", "ef"])
solution("abcdefg")  # ["ab", "cd", "ef", "g_"])
solution("")  # []

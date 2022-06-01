def solution(string, ending):
    """
    Complete the solution so that it returns true
    if the first argument(string) passed in ends
    with the 2nd argument (also a string).
    """

    return string.endswith(ending)


# TESTS
assert solution('abcde', 'abc') == False
assert solution('abcde', 'cde') == True
assert solution('abcde', '') == True

def reverse_letter(string):
    """
    Given a string str, reverse it omitting all non-alphabetic characters.
    """

    return ''.join([ch for ch in string if ch.isalpha()][::-1])


print(reverse_letter('ab22c3d'))
# TESTS
# assert reverse_letter("krishan") == "nahsirk"
# assert reverse_letter("ultr53o?n") == "nortlu"
# assert reverse_letter("ab23c") == "cba"
# assert reverse_letter("krish21an") == "nahsirk"

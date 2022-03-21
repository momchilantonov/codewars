def sum_digits(number):
    """
    Write a function named sum_digits which takes a number as input and
    returns the sum of the absolute value of each of the number's decimal digits.
    """

    return sum(int(n) for n in str(number) if n.isdigit())


# TESTS
assert sum_digits(10) == 1, 'Try again'
assert sum_digits(99) == 18, 'Try again'
assert sum_digits(-32) == 5, 'Try again'

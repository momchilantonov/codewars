def is_eureka(number):
    """Check if the number is eureka"""

    current_number = 0

    if number > 9:
        for i in range(1, len(str(number))+1):
            count_numbern = str(number)[i-1]
            current_number += int(count_numbern)**i
    else:
        return True

    if number == current_number:
        return True

    return False


def sum_dig_pow(a, b):
    """
    The number 89 is the first integer with more than one digit 
    that fulfills the property partially introduced in the title of this kata.
    What's the use of saying "Eureka"? Because this sum gives the same number.
    In effect: 89 = 8^1 + 9^2
    The next number in having this property is 135.
    See this property again: 135 = 1^1 + 3^2 + 5^3
    We need a function to collect these numbers, that may receive two integers a, b
    that defines the range [a, b] (inclusive) and outputs a list of the sorted numbers
    in the range that fulfills the property described above.
    """

    result = []

    for number in range(a, b+1):
        if is_eureka(number):
            result.append(number)

    return result


# TESTS
assert sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
assert sum_dig_pow(10, 89) == [89]
assert sum_dig_pow(10, 100) == [89]
assert sum_dig_pow(90, 100) == []
assert sum_dig_pow(89, 135) == [89, 135]

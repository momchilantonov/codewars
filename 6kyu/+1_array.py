def is_empty_input(input_messages):
    """Check if input is empty"""

    if not input_messages:
        return True

    return False


def is_not_integer(input_messages):
    """Check if all elements are integers"""

    for message in input_messages:
        if not isinstance(message, int):
            return True

    return False


def is_not_negative_digit(input_messages):
    """Check if all digits are positive"""

    for message in input_messages:
        if message < 0:
            return True

    return False


def is_not_single_digit(input_messages):
    """Check if all digits are single"""

    for message in input_messages:
        if message > 9:
            return True

    return False


def is_valid_input(input_messages):
    """Check if the input is valid"""

    if is_empty_input(input_messages) \
            or is_not_integer(input_messages) \
            or is_not_negative_digit(input_messages) \
            or is_not_single_digit(input_messages):
        return False

    return True


def up_array(arr):
    """
    Given an array of integers of any length,
    return an array that has 1 added to the value represented by the array.
        -the array can't be empty
        -only non-negative, single digit integers are allowed
    Return None for invalid inputs.
    """

    if is_valid_input(arr):
        return [int(i) for i in str(int(''.join(str(n) for n in arr)) + 1)]

    return None


# TESTS
assert up_array([2, 3, 9]) == [2, 4, 0]
assert up_array([4, 3, 2, 5]) == [4, 3, 2, 6]
assert up_array([1, -9]) == None

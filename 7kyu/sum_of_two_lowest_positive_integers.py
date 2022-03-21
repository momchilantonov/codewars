def sum_two_smallest_numbers(numbers):
    """
    Create a function that returns the sum of the two lowest positive
    numbers given an array of minimum 4 positive integers.
    No floats or non-positive integers will be passed.
    """

    sum_numbers = 0

    for i in range(2):
        sum_numbers += numbers.pop(numbers.index(min(numbers)))

    return sum_numbers
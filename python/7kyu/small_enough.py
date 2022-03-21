def small_enough(array, limit):
    """
    You will be given an array and a limit value.
    You must check that all values in the array are below or equal to the limit value.
    If they are, return true. Else, return false.
    You can assume all values in the array are numbers.
    """

    for el in array:
        if el > limit:
            return False

    return True


# TESTS
assert small_enough([66, 101], 200) == True
assert small_enough([78, 117, 110, 99, 104, 117, 107, 115] ,100) == False
assert small_enough([101, 45, 75, 105, 99, 107], 107) == True
assert small_enough([80, 117, 115, 104, 45, 85, 112, 115] ,120) == True
assert small_enough([1, 1, 1, 1, 1, 2] ,1) == False
assert small_enough([78, 33, 22, 44, 88, 9, 6] ,87) == False
assert small_enough([1, 2, 3, 4, 5, 6, 7, 8, 9] ,10) == True
assert small_enough([12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12] ,12) == True

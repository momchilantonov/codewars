def count_bits(n):
    """
    Write a function that takes an integer as input, 
    and returns the number of bits that are equal to one 
    in the binary representation of that number. 
    You can guarantee that input is non-negative.
    """

    result = ""
    f_num = f"{n:08b}"

    for el in f_num:
        if el == "1":
            result += el

    return len(result)

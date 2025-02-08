def row_sum_odd_numbers(n):
    """
    Given the triangle of consecutive odd numbers
    """

    result = 0
    start = (n * n)-(n - 1)
    end = start+n * 2
    
    for i in range(start, end, 2):
        result += i

    return result
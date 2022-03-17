def divisors(n):
    """
    Count the number of divisors of a positive integer n.
    Random tests go up to n = 500000.
    """
    
    return len([i for i in range(1, n+1) if n % i == 0])

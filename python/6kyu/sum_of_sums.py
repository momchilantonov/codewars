def sum_of_sums(n):
    """
    S(N) — sum of all positive numbers not more than N
    S(N) = 1 + 2 + 3 + ... + N
    Z(N) — sum of all S(i), where 1 <= i <= N
    Z(N) = S(1) + S(2) + S(3) + ... + S(N)
    You will be given an integer N as input; your task is to return the value of S(Z(N)).
    For example, let N = 3:
    Z(3) = 1 + 3 + 6 = 10
    S(Z(3)) = S(10) = 55
    The input range is 1 <= N <= 10^9 and there are 80 ( 40 in LC ) test cases, of which most are random.
    """
    s_n_squares = n * (n + 1) * (2 * n + 1) // 6
    s_n_integers = n * (n + 1) // 2
    z_n = (s_n_squares + s_n_integers) // 2
    return z_n * (z_n + 1) // 2

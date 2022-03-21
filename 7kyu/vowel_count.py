def get_count(sentence):
    """
    Return the number (count) of vowels in the given string.
    We will consider a, e, i, o, u as vowels for this Kata (but not y).
    The input string will only consist of lower case letters and/or spaces.
    """

    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for ch in sentence:
        if ch in vowels:
            count += 1

    return count

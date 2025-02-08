def duplicate_count(text):
    """
    Write a function that will return the count of distinct
    case-insensitive alphabetic characters and numeric digits
    that occur more than once in the input string.
    The input string can be assumed to contain only alphabets
    (both uppercase and lowercase) and numeric digits.
    """

    text = text.lower()
    chars = {}
    count = 0

    for ch in text:
        if ch not in chars:
            chars[ch] = 1
        else:
            chars[ch] += 1

    for val in chars.values():
        if val > 1:
            count += 1

    return count

def reverse_alternate(string):
    """
    Reverse every other word in a given string, then return the string.
    Throw away any leading or trailing whitespace,
    while ensuring there is exactly one space between each word.
    Punctuation marks should be treated as if they are a part of the word in this kata.
    """
    words = string.strip().split()
    for i in range(1, len(words), 2):
        words[i] = words[i][::-1]
    return " ".join(words)

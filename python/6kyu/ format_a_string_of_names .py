def namelist(names):
    """
    Given: an array containing hashes of names
    Return: a string formatted as a list of names separated
     by commas except for the last two names, which should be separated by an ampersand.
    """

    if len(names) > 1:
        return f'{", ".join(name["name"] for name in names[:-1])} & {names[-1]["name"]}'
    elif len(names) == 1:
        return names[0]['name']
    return ''

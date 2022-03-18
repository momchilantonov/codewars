import re


def validate_pin(pin):
    """
    ATM machines allow 4 or 6 digit PIN codes and PIN codes 
    cannot contain anything but exactly 4 digits or exactly 6 digits.
    If the function is passed a valid PIN string, return true, else return false.
    """

    r1 = r'(?<![\d-])\d{4}(?![a-zA-Z\d\s\.])'
    r2 = r'(?<![\d-])\d{6}(?![a-zA-Z\d\s\.])'

    pattern1 = re.compile(r1)
    pattern2 = re.compile(r2)

    if pattern1.match(pin) or pattern2.match(pin):
        return True

    return False

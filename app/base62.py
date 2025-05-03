ALPHABET = tuple('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
BASE_DICT = {char: index for index, char in enumerate(ALPHABET)}


def encode(num: int) -> str:
    """Encodes a number to a base62 string."""
    if not num:
        return ALPHABET[0]

    encoding = ''
    while num:
        num, rem = divmod(num, 62)
        encoding = ALPHABET[rem] + encoding
    return encoding


def decode(s: str) -> int:
    """Decodes a base62 string to a number."""
    num = 0
    for char in s:
        num = num * 62 + BASE_DICT[char]
    return num

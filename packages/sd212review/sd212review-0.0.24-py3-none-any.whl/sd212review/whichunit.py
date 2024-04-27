import hashlib

def whichunit(alpha: int | str) -> int:
    """Tells which unit to write review questions for based on your alpha."""
    if isinstance(alpha, str):
        alnum = int(alpha[-6:])
    else:
        alnum = alpha
    return int.from_bytes(hashlib.md5(('Mw' + str(alnum)).encode()).digest()) % 11 + 1

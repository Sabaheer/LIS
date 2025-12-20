def calculate_bcc(data: bytes) -> int:
    bcc = 0
    for b in data:
        bcc ^= b
    return bcc

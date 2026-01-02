STX = 0x02
ETX = 0x03

def calculate_bcc(frame: bytes) -> int:
    """
    Calculate BCC as XOR of bytes between STX and ETX (inclusive of ETX)
    """
    in_block = False
    bcc = 0

    for b in frame:
        if b == STX:
            in_block = True
            continue
        if in_block:
            bcc ^= b
        if b == ETX:
            break

    return bcc


def validate_bcc(frame: bytes) -> bool:
    """
    Validate received BCC
    """
    if len(frame) < 3:
        return False

    received_bcc = frame[-1]
    calculated_bcc = calculate_bcc(frame[:-1])

    return received_bcc == calculated_bcc

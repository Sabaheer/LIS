from serial_comm.bcc import calculate_bcc

STX = b'\x02'
ETX = b'\x03'

def build_S_delta(sample_type: bytes, sample_id: bytes):
    body = (
        b"S " +                 # S∆
        b"00" +                 # System No
        sample_type +           # MUST match R∆ (U / S)
        b"    " +               # Dummy
        b"1" +                  # Data classification No
        b" " +                  # Sex
        sample_id +             # SAME sample ID
        b"01" + b"02"           # Test codes
    )

    bcc = calculate_bcc(body + ETX)
    return STX + body + ETX + bytes([bcc])


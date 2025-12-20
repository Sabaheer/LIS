from serial_comm.bcc import calculate_bcc

STX = b'\x02'
ETX = b'\x03'

def build_S_delta():
    body = (
        b"S " +
        b"00" +
        b" " +
        b"    " +
        b"E" +
        b" " +
        b"01" + b"02"
    )

    bcc = calculate_bcc(body + ETX)
    return STX + body + ETX + bytes([bcc])

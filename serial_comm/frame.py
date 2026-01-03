

STX = 0x02
ETX = 0x03

def receive_message(ser):
    buffer = bytearray()

    # Wait for STX
    while True:
        b = ser.read(1)
        if b and b[0] == STX:
            buffer.append(b[0])
            break

    # Read until ETX
    while True:

        b = ser.read(1)
        if not b:
            raise TimeoutError("Receive timeout")

        buffer.append(b[0])
        if b[0] == ETX:
            break

    # Read BCC
    bcc = ser.read(1)
    buffer.append(bcc[0])

    return bytes(buffer)





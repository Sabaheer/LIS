import serial
from config.settings import PORT, BAUDRATE, TIMEOUT

def open_serial():
    return serial.Serial(
        port=PORT,
        baudrate=BAUDRATE,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=TIMEOUT
    )

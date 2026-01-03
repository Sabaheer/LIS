import serial
from config.settings import (
    PORT,
    BAUDRATE,
    BYTESIZE,
    PARITY,
    STOPBITS,
    SERIAL_READ_TIMEOUT
)

def open_serial():
    ser = serial.Serial(
        port=PORT,
        baudrate=BAUDRATE,
        bytesize=BYTESIZE,
        parity=PARITY,
        stopbits=STOPBITS,
        timeout=SERIAL_READ_TIMEOUT  
    )
    return ser

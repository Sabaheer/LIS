from config.settings import PROTOCOL_CLASS
from serial_comm.control_chars import ACK, NAK

def send_ack(ser):
    if PROTOCOL_CLASS == "B":
        ser.write(ACK)

def send_nak(ser):
    if PROTOCOL_CLASS == "B":
        ser.write(NAK)

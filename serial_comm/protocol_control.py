import time
from config.settings import PROTOCOL_CLASS, T4_WAIT_ACK, T6_AFTER_NAK
from serial_comm.control_chars import ACK, NAK

def send_ack(ser):
    if PROTOCOL_CLASS == "B":
        ser.write(ACK)

def send_nak(ser):
    if PROTOCOL_CLASS == "B":
        ser.write(NAK)

def wait_for_ack(ser):
    """
    AU Class B – T4 ACK/NAK wait
    """
    start = time.time()

    while time.time() - start < T4_WAIT_ACK:
        resp = ser.read(1)

        if not resp:
            continue

        if resp == ACK:
            print("RX: ACK")
            return True

        if resp == NAK:
            print("RX: NAK")
            time.sleep(T6_AFTER_NAK)  # T6 delay
            return False

    raise TimeoutError("T4 ACK timeout")

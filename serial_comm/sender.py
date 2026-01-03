from serial_comm.protocol_control import wait_for_ack
from config.settings import MAX_RETRIES

def send_frame_with_ack(ser, frame: bytes):
    """
    AU Class B send with ACK/NAK handling
    """
    for attempt in range(MAX_RETRIES):
        ser.write(frame)

        try:
            if wait_for_ack(ser):
                return True
        except TimeoutError:
            pass

        print(f"NAK or timeout, retry {attempt + 1}")

    raise RuntimeError("Max retries exceeded")

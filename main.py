from serial_comm.connection import open_serial
from serial_comm.frame import receive_message
from protocol.parser import get_message_type
from workflow.sample_request import handle_sample_request

ACK = b'\x06'

def main():
    ser = open_serial()
    print("Analyzer interface started...")

    while True:
        msg = receive_message(ser)
        print("RAW:", msg)

        # Always ACK first (Class B)
        ser.write(ACK)

        msg_type = get_message_type(msg)
        print("Received:", msg_type)

        if msg_type == "R ":
            handle_sample_request(ser, msg)

if __name__ == "__main__":
    main()




def get_message_type(msg: bytes) -> str:
    return msg[1:3].decode("ascii")


def parse_R_delta(msg: bytes):
    # Example: STX R∆ 00 U .... sample_id ETX BCC
    body = msg[1:-2]

    sample_type = body[4:5]      # U / S
    sample_id = body[10:22]      # adjust based on actual message

    return sample_type, sample_id

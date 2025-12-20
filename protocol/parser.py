def get_message_type(msg: bytes) -> str:
    return msg[1:3].decode("ascii")

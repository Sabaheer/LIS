from protocol.builder import build_S_delta
from protocol.parser import parse_R_delta

def handle_sample_request(ser, msg):
    sample_type, sample_id = parse_R_delta(msg)
    response = build_S_delta(sample_type, sample_id)
    ser.write(response)


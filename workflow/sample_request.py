from protocol.builder import build_S_delta

def handle_sample_request(ser):
    response = build_S_delta()
    ser.write(response)

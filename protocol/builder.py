from serial_comm.bcc import calculate_bcc

STX = b'\x02'
ETX = b'\x03'

def build_S_delta(sample_type: bytes, sample_id: bytes):
    body = (
        b"S " +                 
        b"00" +                
        sample_type +           
        b"    " +              
        b"1" +                 
        b" " +                 
        sample_id +            
        b"01" + b"02"           
    )

    bcc = calculate_bcc(body + ETX)
    return STX + body + ETX + bytes([bcc])


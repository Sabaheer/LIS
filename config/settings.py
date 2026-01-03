# Serial layer (T1 / T2 related)
PORT = "/dev/tty.URT2"
BAUDRATE = 9600
BYTESIZE = 8
PARITY = "N"
STOPBITS = 1

# Serial read timeout (T2)
SERIAL_READ_TIMEOUT = 1.0   

# Protocol
PROTOCOL_CLASS = "B"        

# Protocol timers 
T1_WAIT_STX = 5.0       
T2_RECV_MESSAGE = 2.0      
T3_INTER_CHAR = 0.5        
T4_WAIT_ACK = 5.0          
T6_AFTER_NAK = 1.0          

MAX_RETRIES = 3


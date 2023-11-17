# Echo client program
import socket

HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) # connect to the sever with ip- host and port- port
    s.sendall(b'90') # send this data - convert into bytes first
    data = s.recv(1024) # receive data (expected length 1024 bytes)
print('Received', repr(data))
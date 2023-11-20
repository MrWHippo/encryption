import socket
from random import randint

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

#a = randint((2**4),(2**6))
a = 17
p = 1000000

def calculation_one(a,p):
    return ((2**(int(a)))%(int(p)))

def calculation_two(B,a):
    key = (int(B))**(int(a))
    return key

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            conn.sendall(p.to_bytes(16,'little'))
            B = s.recv(1024)
            A = calculation_one(a,p)
            conn.sendall(bytes(A))
            key = calculation_two(B,a)
            print(key)
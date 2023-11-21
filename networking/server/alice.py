import socket
from random import randint
from time import sleep

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50009              # Arbitrary non-privileged port

#a = randint((2**4),(2**6))
a = 17
p = 1000000

def calculation_one(a,p):
    return ((2**(int(a)))%(int(p)))

def calculation_two(B,a,p):
    key = ((int(B))**(int(a))%(int(p)))
    return key

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    A = calculation_one(a,p)
    with conn:
        print('Connected by', addr)
        conn.sendall(bytes(str(p),'utf-8'))
        sleep(0.1)
        conn.sendall(bytes(str(A),'utf-8'))
        B = conn.recv(1024).decode('utf-8')
        key = calculation_two(B,a,p)

print("key:", key)

import socket
from random import randint

HOST = '127.0.0.1' 
PORT = 50007              

#b = randint((2**4),(2**6))
b = 28

def calculation_one(b,p):
    print(b)
    print(p)
    return ((2**(int(b)))%int(p))

def calculation_two(A,b):
    key = (int(A))**(int(b))
    return key

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    p = (s.recv(1024)).decode('utf-8')
    B = calculation_one(b,p)
    s.sendall(bytes(B))
    A = (s.recv(1024)).decode()
    key = calculation_two(A,b)
    print(key)


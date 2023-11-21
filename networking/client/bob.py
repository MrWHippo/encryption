import socket
from random import randint
from time import sleep

HOST = '127.0.0.1' 
PORT = 50009              

#b = randint((2**4),(2**6))
b = 28

def calculation_one(b,p):
    return ((2**(int(b)))%int(p))

def calculation_two(A,b,p):
    key = ((int(A))**(int(b))%(int(p)))
    return key

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    p = s.recv(1024).decode('utf-8')
    B = calculation_one(b,p)
    A = s.recv(1024).decode('utf-8')
    sleep(0.1)
    s.sendall(bytes(str(B), 'utf-8'))
    key = calculation_two(A,b,p)

print("key:", key)


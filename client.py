#!/usr/bin/python

import socket

TCP_IP = 'localhost'
TCP_PORT = 1337
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((TCP_IP, TCP_PORT))
    s.send(bytes("ready", 'utf-8'))
    data = s.recv(BUFFER_SIZE)
finally:
    s.close()

print("Received: ", data)

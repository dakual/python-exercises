#!/usr/bin/python

import socket

sock = socket.socket()
host = socket.gethostname()
port = 1234

sock.connect((host, port))
print(sock.recv(1024))
sock.close() 
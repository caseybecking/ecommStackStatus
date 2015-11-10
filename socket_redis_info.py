#!/usr/bin/env python2

import socket
def client(string):
    HOST, PORT = '172.24.16.68', 6386
    # SOCK_STREAM == a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.setblocking(0)  # optional non-blocking
    sock.connect((HOST, PORT))
    sock.send(string)
    reply = sock.recv(16384)  # limit reply to 16K
    sock.close()
    return reply

#assert client('2+2') == '4'
print client("INFO")
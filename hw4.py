#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost',5566)
sock.bind(server_address)

accounts = []

print "Server start..."

while True:
    data, address = sock.recvfrom(4096)
    if data:
        """sent = sock.sendto(data, address)"""








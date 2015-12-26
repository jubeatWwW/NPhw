#!/usr/bin/env python2.7

import socket
import sys
import getopt
import thread
import re
from test import test
from init import cmdinit
from ls import cmdls
from wt import cmdwt
from rd import cmdrd
from rm import cmdrm
from reply import cmdre
from fwd import cmdfwd
from data import *

HOST = "140.113.235.151"
PORT = 55677

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((HOST,PORT))
sock.listen(10)


def quotesHandler(quoteschk):
    islegal = True
    quoteclose = False

    for i in range(0,len(quoteschk)):
        if not quoteschk[i].isdigit() and not quoteschk[i].isalpha() and quoteschk[i] != '_'\
        and quoteschk[i] != '-' and quoteschk[i] != ':' and quoteschk[i] != '.' and quoteschk[i] != '@'\
        and quoteschk[i] != ' ' and quoteschk[i] != '\"':
            return quoteschk, False
        if quoteschk[i]=='\"' and quoteclose == False:
            quoteclose = True
        elif quoteschk[i]==' ' and quoteclose == True:
            quoteschk = quoteschk[:i]+'^'+quoteschk[i+1:]
        elif quoteschk[i]=='\"' and quoteclose == True:
            quoteclose = False
    while quoteschk[-1:] == ' ':
        quoteschk = quoteschk[:-1]
    return quoteschk, True

def getUserName(addr):
    for i in users:
        if i[1] == addr[1]:
            return i[0]
    return "NotFound"

def shell(s,addr):
    while True:
        data = s.recv(2048)
        data, legalstate = quotesHandler(data)

        if legalstate == False:
            s.sendall("args error(quotesHandler)\n")

        commandlist = data.split()
        command = commandlist[0]
        commandlist.pop(0)

        if command == "exit":
            user = getUserName(addr)
            if user != "NotFound":
                for userdel in users:
                    if userdel[0] == user:
                        users.remove(userdel)
                        break
            s.sendall("exit\n")
            s.close()
            break
        elif command == "init":
            s.sendall(cmdinit(commandlist,addr))
            continue
        elif command == "ls":
            s.sendall(cmdls(commandlist,getUserName(addr)))
            continue
        elif command == "wt":
            s.sendall(cmdwt(commandlist,getUserName(addr)))
            continue
        elif command == "rd":
            s.sendall(cmdrd(commandlist,getUserName(addr)))
            continue
        elif command == "rm":
            s.sendall(cmdrm(commandlist,getUserName(addr)))
            continue
        elif command == "re":
            s.sendall(cmdre(commandlist,getUserName(addr)))
            continue
        elif command == "fwd":
            s.sendall(cmdfwd(commandlist,getUserName(addr)))
            continue
        s.sendall("Hello\n")

while True:
    addr = (HOST, PORT)
    connection, address = sock.accept()
    thread.start_new_thread(shell,(connection,address))

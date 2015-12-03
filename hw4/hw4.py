#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import socket
import sys
import json
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost',55668)
sock.bind(server_address)

accounts = []

print "Server start..."

def getAccID(addr):
    for account in accounts:
        if addr == account[3]:
            return accounts.index(account)
    return -1

def sendOKMsg(addr):
    retdata = {'message':"ok"}
    sent = sock.sendto(json.dumps(retdata), addr)

def sendErrMsg(addr, msg):
    retdata = {'message':msg}
    sent = sock.sendto(json.dumps(retdata), addr)

def searchAccByName(name):
    for account in accounts:
        if name == account[0]:
            return accounts.index(account)
    return -1

def searchAccByID(id):
    for account in accounts:
        if id == account[1]:
            return accounts.index(account)
    return -1



while True:
    data, address = sock.recvfrom(4096)

    if data:
        recvdata = json.loads(data)
        if recvdata['action'] == "init":
            idchk = searchAccByID(recvdata['account_id'])
            if idchk >= 0:
                sendErrMsg(address, "account_id has been registered")
            else:
                accounts.append([recvdata['account_name'], recvdata['account_id'], int(0), address[1]])
                sendOKMsg(address)
        elif recvdata['action'] == "save":
            curID = getAccID(address[1])
            if curID >= 0:
                accounts[curID][2] += recvdata['money']
                sendOKMsg(address)
            else:
                sendErrMsg(address, "error: account not find")
        elif recvdata['action'] == "withdraw":
            curID = getAccID(address[1])
            if curID >=0:
                if accounts[curID][2] >= recvdata['money']:
                    accounts[curID][2] -= recvdata['money']
                    sendOKMsg(address)
                else:
                    sendErrMsg(address, "invalid transaction")
            else:
                sendErrMsg(address, "error: account not find")
        elif recvdata['action'] == "remit":
            curID = getAccID(address[1])
            desID = searchAccByName(recvdata['destination_name'])
            if curID >=0 and desID >=0 and curID != desID:
                if accounts[curID][2] >= recvdata['money']:
                    accounts[curID][2] -= recvdata['money']
                    accounts[desID][2] += recvdata['money']
                    sendOKMsg(address)
                else:
                    sendErrMsg(address, "invalid transaction")
            elif curID == desID:
                sendErrMsg(address, "invalid transaction")
            elif desID < 0:
                sendErrMsg(address, "invalid transaction")
            else:
                sendErrMsg(address, "error: account not find")
        elif recvdata['action'] == "show":
            curID = getAccID(address[1])
            if curID >=0:
                retdata = {'message':accounts[curID][2]}
                sent = sock.sendto(json.dumps(retdata),address)
            else:
                sendErrMsg(address, "error: account not find")
        elif recvdata['action'] == "bomb":
            for i in range(0,len(accounts)):
                accounts[i][2] = 0
            sendOKMsg(address)
        elif recvdata['action'] == "end":
            accounts = []
            retdata = {'message':"end"}
            sent = sock.sendto(json.dumps(retdata),address)
        """print accounts"""







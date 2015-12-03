#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import socket
import sys
import json
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('140.113.123.225',5567)
sock.bind(server_address)

accounts = []

savelist = []
remitlist = []
bombcnt = [0,0]

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
    print "error: "+msg

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
        for i in savelist:
            if i[2] == 0:
                accounts[i[0]][2] += i[1]
                print accounts[i[0]][0]+"  "+str(i[1])+" saved"
                print accounts[i[0]][0]+"'s deposit: "+str(accounts[i[0]][2])
                savelist.remove(i)

        for i in remitlist:
            if i[3] == 0:
                accounts[i[2]][2] += i[1]
                print accounts[i[2]][0]+"  "+str(i[1])+" get"
                print accounts[i[2]][0]+"'s deposit: "+str(accounts[i[2]][2])
                remitlist.remove(i)

        if bombcnt[0]==1 and bombcnt[1]==0:
            for i in range(0,len(accounts)):
                accounts[i][2] = 0
                print "boom!!!"
                bombcnt = [0,0]

        print "Receive Action: "+recvdata['action']

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
                """accounts[curID][2] += recvdata['money']"""
                sendOKMsg(address)
                savelist.append([curID,recvdata['money'],2])
                print accounts[curID][0]+" request to save "+str(recvdata['money'])
            else:
                sendErrMsg(address, "error: account not find")
        elif recvdata['action'] == "withdraw":
            curID = getAccID(address[1])
            if curID >=0:
                if accounts[curID][2] >= recvdata['money']:
                    accounts[curID][2] -= recvdata['money']
                    sendOKMsg(address)
                    print accounts[curID][0]+" withdraw "+str(recvdata['money'])
                    print accounts[curID][0]+"'s deposit: "+str(accounts[curID][2])
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
                    """accounts[desID][2] += recvdata['money']"""
                    sendOKMsg(address)
                    print accounts[curID][0]+" send "+str(recvdata['money'])
                    print accounts[curID][0]+"'s deposit: "+str(accounts[curID][2])
                    remitlist.append([curID,recvdata['money'],desID,3])
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
            """for i in range(0,len(accounts)):
                accounts[i][2] = 0"""
            sendOKMsg(address)
            bombcnt = [1, 5]
        elif recvdata['action'] == "end":
            accounts = []
            retdata = {'message':"end"}
            sent = sock.sendto(json.dumps(retdata),address)

        for i in range(0,len(savelist)):
            savelist[i][2] -= 1
        for i in range(0,len(remitlist)):
            remitlist[i][3] -= 1
        if bombcnt[0] == 1:
            bombcnt[1] -= 1
        print "-----------------------------"
        """
        print "-----------------------------"
        print accounts
        print savelist
        print remitlist
        print bombcnt"""







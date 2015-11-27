# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 23:09:38 2015

@author: Justin-PC
"""
#!/usr/bin/python2.7


HOST = '140.113.123.225'
PORT = 5566

import socket
import json
import sys
import getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:p:")
except getopt.GetoptError:
    print 'hw1.py -i <HOST> -p <PORT>'
    sys.exit

for opt, arg in opts:
    if opt=='-h':
        print 'hw1.py -i <HOST> -p <PORT>'
        sys.exit
    elif opt=='-i':
        HOST = arg
    elif opt=='-p':
        PORT = int(arg)
    else:
        print "unknown opts "+arg


address = (HOST,PORT)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

minGuess = 2999
maxGuess = 60001
portGuess = 31500
toClose = 0



"""
HOST = raw_input("Input host: ")
PORT = raw_input("Input port: ")
"""
while True:
        Obj = {"guess":portGuess}
        jsonObj = json.dumps(Obj)
        s.sendto(jsonObj, address)
        print "send:"+jsonObj
        data, addr = s.recvfrom(2048)
        recvJson = json.loads(data)
        print "receive:"+data
        if recvJson['result'] == "larger":
            minGuess = portGuess
            portGuess = (portGuess+maxGuess)/2
        elif recvJson['result'] == "smaller":
            maxGuess = portGuess
            portGuess = (portGuess+minGuess)/2
        else:
            ans = {"student_id":"0216053"}
            ansJson = json.dumps(ans)
            s.sendto(ansJson,(HOST,portGuess))
            print "send:"+ansJson
            data, addr = s.recvfrom(2048)
            recvJson = json.loads(data)
            print "receive:"+data+"\n"
            break
s.close()

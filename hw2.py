#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 18:21:07 2015

@author: Justin-PC
"""

import socket
import json
import sys
import getopt

HOST = "127.0.0.1"
PORT = 5566
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:p:")
except getopt.GetoptError:
    print 'hw2.py -i <HOST> -p <PORT>'
    sys.exit

for opt, arg in opts:
    if opt=='-h':
        print 'hw2.py -i <HOST> -p <PORT>'
        sys.exit
    elif opt=='-i':
        HOST = arg
    elif opt=='-p':
        PORT = int(arg)
    else:
        print "unknown opts "+arg


address = (HOST,PORT)
connection_state = False
game_state = False
data = {"action":"input"}




def main():

    print "Wlecome to Game 2048!"
    print "enter 'help' to get more information"
    print " "

    while True:
        if game_state == False:
            command = raw_input(">")
        else:
            command = raw_input("move>")
        sysmsg = menu(command)
        #print sysmsg
        if sysmsg == "n":
            continue
        elif sysmsg == "exit":
            break
        else:
            if sysmsg['status'] == 1:
                show_grid(sysmsg['message'])
            else:
                print sysmsg['message']
    print "Thanks for playing!"
    print "See you again!"
    s.close

def menu(command):
    global connection_state
    global s
    global game_state
    if command == "connect":
        if connection_state == False:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect(address)
            connection_state = True
        else:
            print "Have already connectted to server"
        return "n"
    elif command == "disconnect":
        s.shutdown(1)
        connection_state = False
        game_state = False
        return "n"
    elif command== "help":
        print "Enter keyboard:"
        print "'connect' - connect to game server"
        print "'disconnect' - disconnect from game server"
        print "'new' - new a game round"
        print "'end' - close the game"
        print "'w' - move bricks up"
        print "'s' - move bricks down"
        print "'a' - move bricks left"
        print "'d' - move bricks right"
        print "'u' - undo the last move"
        print "'exit' - leave the game"
        return "n"
    elif command == "exit":
        return "exit"
    else:
        if connection_state == True:
            if command == "new":
                if game_state == False:
                    data['action'] = "New"
                    game_state = True
                else:
                    print "Have already in a game round"
                    return "n"
            elif command == "end":
                data['action'] = "End"
                game_state = False
                print "The game has closed"
                return "n"
            else:
                if game_state == True:
                    if command == "w":
                        data['action'] = "moveUp"
                    elif command == "s":
                        data['action'] = "moveDown"
                    elif command == "a":
                        data['action'] = "moveLeft"
                    elif command == "d":
                        data['action'] = "moveRight"
                    elif command == "u":
                        data['action'] = "unDo"
                    elif command == "whosyourdaddy":
                        data['action'] = "whosyourdaddy"
                    else:
                        print "Unknown command"
                        return "n"
                else:
                    print "Please new a game round first"
                    return "n"
            msg = json.dumps(data)
            s.sendall(msg)
            recvdata = s.recv(2048)
            return json.loads(recvdata)
        else:
            print "Please connect to server first"
            return "n"

def show_grid(nums):
    print '----------------------'
    numArr = nums.split(',')

    for i in range(0,4):
        str = "|"
        for j in range(0,4):
            if numArr[i*4+j] == "0":
                str+= '    |'
            else:
                str+='%4d|' % (int(numArr[i*4+j]))
        print str
        print '----------------------'

    if "2048" in [x for x in numArr]:
        print "\n\nCongrates! You win the game!"
        menu("end")




if __name__ == "__main__":
    main()






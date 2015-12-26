import getopt
from data import *

def digitFilter(judge):
    if judge.isdigit():
        return True
    else:
        return False


def cmdrd(commandlist, user):
    if user == "NotFound":
        return "init first\n"
    try:
        opts, args = getopt.getopt(commandlist,"r:")
        if len(args) > 0:
            return "option error\n"
        for opt, arg in opts:
            if opt == "-r":
                if digitFilter(arg):
                    if int(arg) <= len(mbox[user]):
                        mail = mbox[user][int(arg)-1][0]
                        mbox[user][int(arg)-1][1] = 'read'
                        return "From:"+str(mail[0])+"@nctu.edu.tw\nTo:"+user+"@nctu.edu.tw\nDate:"+str(mail[1])+"\nTitle:"+str(mail[2])+"\nContent:"+str(mail[3])+"\n"
                    else:
                        return "args error\n"
                else:
                    return "args error\n"
    except getopt.GetoptError:
        return "option error(except)\n"

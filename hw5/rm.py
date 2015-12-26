import getopt
from data import *
from rd import digitFilter

def cmd_rm_opt_d(user, num):
    if digitFilter(num):
        if int(num) <= len(mbox[user]):
            mbox[user].remove(mbox[user][int(num)-1])
            return "done\n"
        else:
            return "args error\n"
    else:
        return "args error\n"

def cmd_rm_opt_D(user):
    mbox[user] = []
    return "done\n"

def cmdrm(commandlist, user):
    if user == "NotFound":
        return "init first\n"
    try:
        opts, args = getopt.getopt(commandlist,"d:D")

        if len(args) > 0:
            return "option error\n"
        for opt,arg in opts:
            if opt == "-d":
                return cmd_rm_opt_d(user,arg)
            elif opt == "-D":
                return cmd_rm_opt_D(user)
    except getopt.GetoptError:
        return "option error(except)\n"

import getopt
from data import *
def usernameChk(username, addr):
    if username[0] == '\"' and username[-1:] == '\"':
        username = username[1:-1]

    for i in username:
        if not i.isdigit() and not i.isalpha() and i != '_' and i != '-':
            return "args error\n"
    if username in [x[0] for x in users]:
        return "This account has been registered\n"
    else:
        users.append((username,addr[1]))
        mbox[username] = []
        return username+"@nctu.edu.tw\n"


def cmdinit(commandlist, addr):
    try:
        opts, args = getopt.getopt(commandlist, "u:")
        for opt, arg in opts:
            if opt == "-u":
                return usernameChk(arg, addr)
    except getopt.GetoptError:
        return "option error(except)\n"

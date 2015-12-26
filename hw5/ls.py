import getopt
from data import *

def cmd_ls_opt_u():
    retmsg = ""
    if len(users) > 0:
        for i in users:
            retmsg += str(i[0])+"@nctu.edu.tw\n"
        return retmsg
    else:
        return "no accounts\n"

def cmd_ls_opt_l(user):
    if user == "NotFound":
        return "init first\n"
    if len(mbox[user]) <= 0:
        return "no mail\n"
    else:
        mailNum = 0
        retmsg = ""
        for mail in mbox[user]:
            mailNum = mailNum+1
            retmsg+=str(mailNum)+". "+str(mail[0][2])
            if mail[1] == "new":
                retmsg+="(new)"
            retmsg+="\n"
        return retmsg

def cmd_ls_opt_a(user):
    if user == "NotFound":
        return "init first\n"
    return "Account:"+user+"\nMail address:"+user+"@nctu.edu.tw\nNumber of mails:"+str(len(mbox[user]))+"\n"

def cmdls(commandlist, user):
    if len(commandlist) > 1:
        return "args error\n"
    try:
        opts, args = getopt.getopt(commandlist,"ula")

        for opt, arg in opts:
            if opt == "-u":
                return cmd_ls_opt_u()
            elif opt == "-l":
                return cmd_ls_opt_l(user)
            elif opt == "-a":
                return cmd_ls_opt_a(user)
    except getopt.GetoptError:
        return "option error\n"

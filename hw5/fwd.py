import getopt
from data import *
from wt import cmdwt
from rd import cmdrd
from rd import digitFilter

def contentParser(content,newcontent):
    retmsg = []
    newTitle = content.split('\n')[3].replace("Title:","")
    if newTitle[:3] == "re:":
        retmsg.append('fwd:'+newTitle[3:])
    elif newTitle[:4] == 'fwd:':
        retmsg.append(newTitle)
    else:
        retmsg.append('fwd:'+newTitle)

    retmsg.append(newcontent+'\n----\n'+content)
    return retmsg

def cmdfwd(commandlist, user):
    if user == "NotFound":
        return "init first\n"

    try:
        opts, args = getopt.getopt(commandlist,"d:c:n:")
        receiver = ""
        content = ""
        newcontent = ""
        for opt, arg in opts:
            if opt == "-d":
                if arg.replace('@nctu.edu.tw','') in [x[0] for x in users]:
                    receiver = arg.replace('@nctu.edu.tw','')
                else:
                    return "args error\n"
            elif opt == "-c":
                newcontent = arg
            elif opt == "-n":
                content = cmdrd(['-r',arg],user)
                if content == "args error\n":
                    return content
        fwdlist = contentParser(content,newcontent)
        return cmdwt(['-d',receiver+"@nctu.edu.tw",'-t',fwdlist[0],'-c',fwdlist[1][:-1]],user)


    except getopt.GetoptError:
        return "option error\n"

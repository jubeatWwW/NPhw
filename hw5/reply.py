import getopt
from data import *
from rd import cmdrd
from wt import cmdwt
from rd import digitFilter

def replycontentParser(content,newcontent):
    retmsg = []
    contentlist = content.split('\n')
    retmsg.append(contentlist[0].replace('From:','').replace('@nctu.edu.tw',''))
    contentlist[3] = contentlist[3].replace('Title:','')
    if contentlist[3][:4] == 'fwd:':
        retmsg.append('re:'+contentlist[3][4:])
    elif contentlist[3][:3] == 're:':
        retmsg.append(contentlist[3])
    else:
        retmsg.append('re:'+contentlist[3])
    retmsg.append(newcontent+"\n----\n"+content)
    return retmsg

def cmdre(commandlist, user):
    if user == "NotFound":
        return "init first\n"
    try:
        opts, args = getopt.getopt(commandlist, "c:n:")
        replycontent = ""
        newcontent = ""
        for opt,arg in opts:
            if opt == "-c":
                newcontent = arg
            elif opt == "-n":
                if digitFilter(arg):
                    replycontent = cmdrd(['-r',arg], user)
                    if replycontent == "args error\n":
                        return "args error\n"
                else:
                    return "args error\n"
        wtlist = replycontentParser(replycontent, newcontent)
        return cmdwt(['-d',wtlist[0],'-t',wtlist[1],'-c',wtlist[2][:-1]],user)
    except getopt.GetoptError:
        return "option error\n"

import getopt
from data import *

def textParser(text):
    if text[0] == '\"' and text[-1:] == '\"':
        return text[1:-1].replace('^',' ')
    else:
        return text


def cmdwt(commandlist, user):
    if user == "NotFound":
        return "init first\n"
    try:
        opts, args = getopt.getopt(commandlist,"d:t:c:")
        if len(args) > 0:
            return "option error\n"
        receiver = ""
        title = ""
        content = ""
        for opt, arg in opts:
            if opt == "-d":
                receiver = arg.replace("@nctu.edu.tw", "")
            elif opt == "-t":
                title = arg
            elif opt == "-c":
                content = arg

        if receiver[0] == '\"' and receiver[-1:] == '\"':
            receiver = receiver[1:-1]

        if receiver in [x[0] for x in users]:
            mbox[receiver].append([(user,"data",textParser(title),textParser(content)),'new'])
            return "done\n"
        else:
            return "args error\n"

    except getopt.GetoptError:
        return "option error(except)\n"
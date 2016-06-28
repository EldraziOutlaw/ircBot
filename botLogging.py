def log(name,logfilename,rawinput):
    logmsg=messagecontent(rawinput)
    with open("./" + logfilename + ".txt", "a") as logfile:
        logfile.write(name + " : " +logmsg + "\n")

def messagecontent(rawinput):
    discard,discard,logmsg = rawinput.split(":",2)
    return logmsg

def defaultlog(rawinput):
    with open("./default.txt", "a") as logfile:
        logfile.write(rawinput + "\n")

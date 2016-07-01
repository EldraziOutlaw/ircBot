import messageHandling

def log(rawinput):
    name = messageHandling.getsender(rawinput)
    logfilename = messageHandling.getlocation(rawinput)
    logmsg=messagecontent(rawinput)
    with open("./" + logfilename + ".txt", "a") as logfile:
        logfile.write(name + " : " +repr(logmsg) + "\n")

def messagecontent(rawinput):
    discard,discard,logmsg = rawinput.split(":",2)
    return logmsg

def defaultlog(rawinput):
    with open("./default.txt", "a") as logfile:
        logfile.write(repr(rawinput) + "\n")

import os, messageHandling, datetime

def havemessage(name):
    if os.path.exists(name) is True:
        return True
    else:
        return False

def leavemessage(message):
    sender=messageHandling.getsender(message)
    print "getting sender " + sender
    discard,message=message.split("&tell ",1)
    name,message=message.split(" ",1)
    with open ("./" + name, "a") as messagefile:
        print "building messagefile"
        messagefile.write(name + ": " + message + " From " + sender + "\r\n")

def givemessage(name):
    message = []
    with open("./" + name, "r") as messagefile:
        for line in messagefile:
            message.append(line)
        os.remove("./" + name)
    return message


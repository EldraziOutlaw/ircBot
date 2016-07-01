def typecheck(rawinput):
    type = ""
    if "\x01" in rawinput:
        if "ACTION" in rawinput:
            type = "ACTION"
        else:
            type = "CTCP"
    elif "PRIVMSG" in rawinput:
        type = "PRIVMSG"
    elif "JOIN" in rawinput:
        type = "JOIN"
    elif "QUIT" in rawinput:
        type = "QUIT"
    elif "PART" in rawinput:
        type = "PART"
    elif "TOPIC" in rawinput:
        type = "TOPIC"
    elif "PING" in rawinput:
        type = "PING"
    elif "PONG" in rawinput:
        type = "PONG"
    else:
        type = "defualt"
    return type

def getsender(rawinput):
    name,discard = rawinput.split("!",1)
    name = name.strip(":")
    return name

def getlocation(rawinput):
    discard,temp = rawinput.split("#",1)
    location,discard = temp.split(" :",1)
    return location

def firstword(rawinput):
    location=getlocation(rawinput)
    discard,temp=rawinput.split(location +" :",1)
    try:
        firstword,discard=temp.split(" ",1)
    except:
        firstword=temp
    return firstword
def typecheck(rawinput):
    type = ""
    if "PRIVMSG" in rawinput:
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
    elif "\x01" in rawinput:
        type = "CTCP"
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
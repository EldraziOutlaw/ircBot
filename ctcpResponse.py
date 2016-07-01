import messageHandling, datetime

def response(rawinput):
    output=""
    type = ""
    sender = messageHandling.getsender(rawinput)
    try:
        discard, ctcp, discards = rawinput.split("\x01", 2)
        if "PING" in ctcp and ctcp.strip("PING") == "":
            type="PING"
            output = getping(rawinput)
        elif "VERSION" in ctcp:
            type="VERSION"
            output = "VERSION 0.0.0.1"
        elif "FINGER" in ctcp:
            type="FINGER"
            output="0///////0"
        elif "SOURCE" in ctcp:
            type="SOURCE"
            output="SOURCE currently unavailable"
        elif "TIME" in ctcp:
            type="TIME"
            output=datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        else:
            discard, type, discard = rawinput.split("\x01")
            output = "I don't know that one"
    except:
        type="UNKNOWN"
        output="UNKNOWN CTCP REQUEST"
    response = "NOTICE " + sender + " :\x01" + type + " " + output + "\x01\r\n"
    return response


def getping(rawinput):
    discard,temp,discard = rawinput.split("\x01")
    pingmsg = temp.strip("PING ")
    return pingmsg
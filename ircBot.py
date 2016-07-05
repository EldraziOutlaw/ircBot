import socket, argparse, botLogging, messageHandling, ctcpResponse, tellModule

parser = argparse.ArgumentParser()
parser.add_argument("-s", dest="server", help="server destination", default="irc.dbcommunity.org")
parser.add_argument("-p", dest="port", help="port number", default=6667, type=int)
parser.add_argument("-c", dest="chan", help="chan", default="desertbus")
parser.add_argument("-n", dest="botnick", help="bot nickname", default="GhostBot")
args = parser.parse_args()
buffsize = 2048
botnick= args.botnick
port = args.port
server = args.server
chan= args.chan
uname = "GhostBot"
realname = "PlsDon'tBreak"


def ping(pongmsg):
    ircsock.send("PONG " + pongmsg + "\r\n")

def testprint():
    file=open("./testDoc", "r")
    for line in file:
        ircsock.send("PRIVMSG #" + chan + " :" + line + "\r\n")


def main():
    global ircsock
    ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ircsock.connect((server,port))
    ircsock.send("USER " + uname + " 2 3 " + " :" + realname + "\r\n")
    ircsock.send("NICK " + botnick + "\r\n")
    ircsock.send("JOIN #" + chan + "\r\n")

    tempmsg = ""

    while True:

        while "\n" not in tempmsg:
            tempmsg += ircsock.recv(buffsize)
        ircmsg, tempmsg = tempmsg.split("\r\n", 1)
        print repr(ircmsg)
        botLogging.defaultlog(ircmsg)
        messagetype=messageHandling.typecheck(ircmsg)

        if messagetype == "PING":
           pongmsg=ircmsg.strip("PING ")
           ping(pongmsg)
        elif messagetype == "CTCP":
            ircsock.send(ctcpResponse.response(ircmsg))
        elif messagetype == "PRIVMSG":
            firstword = messageHandling.firstword(ircmsg)
            try:
                botLogging.log(ircmsg)
                if tellModule.havemessage(messageHandling.getsender(ircmsg)):
                    message=tellModule.givemessage(messageHandling.getsender(ircmsg))
                    for lines in message:
                        ircsock.send("PRIVMSG #" + chan + " :" + lines)
                if firstword == "&tell":
                    ircsock.send("PRIVMSG #" + chan + " :OK, I will tell them that next time they speak\r\n")
                    tellModule.leavemessage(ircmsg)
                if firstword == "&help":
                    name=messageHandling.getsender(ircmsg)
                    ircsock.send("NOTICE " + name + " nu\r\n")
            except Exception as e:
                print e


try:
    main()
except KeyboardInterrupt:
    pass
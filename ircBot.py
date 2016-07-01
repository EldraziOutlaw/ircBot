import socket, argparse, botLogging, messageHandling, ctcpResponse, tellModual

parser = argparse.ArgumentParser()
parser.add_argument("-s", dest="server", help="server destination", default="irc.dbcommunity.org")
parser.add_argument("-p", dest="port", help="port number", default=6667, type=int)
parser.add_argument("-c", dest="chan", help="chan", default="desertbus")
args = parser.parse_args()
botnick = "EldraziBot"
buffsize = 2048
port = args.port
server = args.server
chan= args.chan
uname = "EldraziBot"
realname = "ToManyNamesIConfuse"


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
                if tellModual.havemessage(messageHandling.getsender(ircmsg)):
                    ircsock.send("PRIVMSG #" + chan + " :" + tellModual.giveessage(messageHandling.getsender(ircmsg)))
                if firstword == "&tell":
                    ircsock.send("PRIVMSG #" + chan + " :OK, I will tell them that next time they speak\r\n")
                    tellModual.leavemessage(ircmsg)
                if firstword == "&help":
                    name=messageHandling.getsender(ircmsg)
                    ircsock.send("NOTICE " + name + " nu\r\n")
            except Exception as e:
                print e


try:
    main()
except KeyboardInterrupt:
    pass
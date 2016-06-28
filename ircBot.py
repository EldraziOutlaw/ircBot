import socket, botLogging, messageHandling

botnick = "EldraziBot"
buffsize = 2048
port = 6667
server = "irc.dbcommunity.org"
uname = "EldraziBot"
realname = "ToManyNamesIConfuse"


def ping(pongmsg):
    ircsock.send("PONG " + pongmsg + "\r\n")


def main():
    global ircsock
    ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ircsock.connect((server,port))
    ircsock.send("USER " + uname + " 2 3 " + " :" + realname + "\r\n")
    ircsock.send("NICK " + botnick + "\r\n")

    tempmsg = ""

    while True:

        while "\n" not in tempmsg:
            tempmsg += ircsock.recv(buffsize)
        ircmsg, tempmsg = tempmsg.split("\r\n", 1)

        print ircmsg
        botLogging.defaultlog(ircmsg)
        messagetype=messageHandling.typecheck(ircmsg)

        if messagetype == "PING":
           pongmsg=ircmsg.strip("PING ")
           ping(pongmsg)
        elif messagetype == "PRIVMSG":
            name=messageHandling.getsender(ircmsg)
            location=messageHandling.getlocation(ircmsg)
            botLogging.log(name,location,ircmsg)


main()
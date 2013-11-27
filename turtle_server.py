import socket
import SocketServer
import turtle


class Command:

    def __init__(self, string):
        self.args = string.split()
        self.opcode = self.args[0]
        del(self.args[0])

    def float(self, index):
        return float(self.args[0])


class Screen:

    COLORS = ['red', 'green', 'blue', 'black', 'grey', 'yellow', 'brown', 'pink', 'cyan']

    def __init__(self):
        self.turtles = {}

    def process(self, who, cmd):
        if not self.turtles.has_key(who):
            self.turtles[who] = turtle.Turtle()
            self.turtles[who].pencolor(self.COLORS[len(self.turtles)-1])
        t = self.turtles[who]
        if cmd.opcode == "F":
            t.forward(cmd.float(0))
        elif cmd.opcode == "B":
            t.backward(cmd.float(0))
        elif cmd.opcode == "L":
            t.left(cmd.float(0))
        elif cmd.opcode == "R":
            t.right(cmd.float(0))
        elif cmd.opcode == "U":
            t.penup()
        elif cmd.opcode == "D":
            t.pendown()
        else:
            t.left(360*2)


screen = Screen()


class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        source_ip, source_port = self.client_address
        print "{}:{} > [{}]".format(source_ip, source_port, self.data)
        cmd = Command(self.data)
        screen.process(source_ip, cmd)
        # just send back the same data, but upper-cased
        #self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = socket.gethostbyname(socket.gethostname()), 1337
    print "Listening on %s:%d" % (HOST, PORT)
    SocketServer.TCPServer.allow_reuse_address = True
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()

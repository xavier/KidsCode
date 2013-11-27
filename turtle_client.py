import socket

class Turtle:

  BUFFER_SIZE = 1024
  DEFAULT_PORT = 1337

  def __init__(self, host, port=DEFAULT_PORT):
    self.host, self.port = host, port

  def forward(self, x):
    self.__send_command("F", x)

  def backward(self, x):
    self.__send_command("B", x)

  def left(self, x):
    self.__send_command("L", x)

  def right(self, x):
    self.__send_command("R", x)

  def penup(self):
    self.__send_command("U")

  def pendown(self):
    self.__send_command("D")

  def speed(self, s):
    pass

  def color(self, _):
    pass

  def setposition(self, x, y):
    pass

  def position(self):
    return (0, 0)

  def hideturtle(self):
    pass

  def showturtle(self):
    pass

  def __send_command(self, *args):
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.socket.connect((self.host, self.port))
    self.socket.send(" ".join(map(str, args)))
    #data = s.recv(BUFFER_SIZE)
    self.socket.close()

Pen = Turtle
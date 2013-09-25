import turtle
import math

t = turtle.Pen()

cote1 = 100.0
cote2 = 50.0
cote3 = math.sqrt(cote1**2 + cote2**2)

angle1 = 90
angle2 = 180-math.degrees(math.atan(cote1/cote2))

t.forward(cote1)
t.left(angle1)
t.forward(cote2)
t.left(angle2)
t.forward(cote3)

raw_input()
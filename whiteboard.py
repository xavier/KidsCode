import turtle

t = turtle.Pen()

distance = 30

def right():
  t.setheading(0)
  t.forward(distance)

def up():
  t.setheading(90)
  t.forward(distance)

def left():
  t.setheading(180)
  t.forward(distance)

def down():
  t.setheading(270)
  t.forward(distance)

turtle.onkey(up,        "Up")
turtle.onkey(down,      "Down")
turtle.onkey(left,      "Left")
turtle.onkey(right,     "Right")

turtle.onkey(t.penup,   "u")
turtle.onkey(t.pendown, "d")
turtle.onkey(t.reset,   "c")

turtle.onscreenclick(t.goto)

turtle.listen()
turtle.mainloop()
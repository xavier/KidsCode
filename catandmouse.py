import turtle

cat      = turtle.Pen()
mouse    = turtle.Pen()

distance = 30

def move(player):
  player.forward(distance)
  if cat.distance(mouse) < 10:
    mouse.hideturtle()
    cat.circle(100)

def catright():
  cat.setheading(0)
  move(cat)

def catup():
  cat.setheading(90)
  move(cat)

def catleft():
  cat.setheading(180)
  move(cat)

def catdown():
  cat.setheading(270)
  move(cat)

def mouseright():
  mouse.setheading(0)
  move(mouse)

def mouseup():
  mouse.setheading(90)
  move(mouse)

def mouseleft():
  mouse.setheading(180)
  move(mouse)

def mousedown():
  mouse.setheading(270)
  move(mouse)

turtle.onkey(catup,      "Up")
turtle.onkey(catdown,    "Down")
turtle.onkey(catleft,    "Left")
turtle.onkey(catright,   "Right")

turtle.onkey(mouseup,    "z")
turtle.onkey(mousedown,  "s")
turtle.onkey(mouseleft,  "q")
turtle.onkey(mouseright, "d")

cat.color("red")
cat.penup()

mouse.color("green")
mouse.penup()
mouse.forward(distance * 3)

turtle.listen()
turtle.mainloop()
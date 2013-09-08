import turtle

t = turtle.Pen()

def augmente(segment, pourcent):
  return segment + (segment*(pourcent/100.0))

def spirale_recursive(t, segment, pourcent, angle, iterations):
  if iterations == 0: return
  t.forward(segment)
  t.right(angle)
  spirale_recursive(t, augmente(segment, pourcent), pourcent, angle, iterations-1)

def spirale_iterative(t, segment, pourcent, angle, iterations):
  for i in range(iterations):
    t.forward(segment)
    t.right(angle)
    segment = augmente(segment, pourcent)

t.speed("fast")

spirale_recursive(t, 10, 15, 50, 30)

t.penup()
t.home()
t.pendown()

spirale_iterative(t, 10, 10, 98, 50)

raw_input()
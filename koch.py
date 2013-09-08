import turtle

t = turtle.Pen()

def courbe(t, longueur_segment, iteration):
  if iteration == 0:
    t.forward(longueur_segment)
  else:
    courbe(t, longueur_segment/3, iteration-1)
    t.left(60)
    courbe(t, longueur_segment/3, iteration-1)
    t.right(120)
    courbe(t, longueur_segment/3, iteration-1)
    t.left(60)
    courbe(t, longueur_segment/3, iteration-1)

def flocon(t, longueur_segment, iteration):
  courbe(t, longueur_segment, iteration)
  t.right(120)
  courbe(t, longueur_segment, iteration)
  t.right(120)
  courbe(t, longueur_segment, iteration)

def flocon_centre(t, longueur_segment, iteration):
  t.penup()
  x, y = t.position()
  t.setposition(x-longueur_segment/2, y+longueur_segment/3)
  t.pendown()
  flocon(t, longueur_segment, iteration)

t.speed('fast')
flocon_centre(t, 300, 3)

t.hideturtle()

raw_input();
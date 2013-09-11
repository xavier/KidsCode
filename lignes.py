import turtle

t = turtle.Pen()
t.hideturtle()

LARGEUR_ECRAN = turtle.window_width()
HAUTEUR_ECRAN = turtle.window_height()

def ligne(t, a, b, couleur):
  etat_precedent = t.pen()
  t.penup()
  t.goto(a)
  t.pendown()
  t.color(couleur)
  t.goto(b)
  t.pen(etat_precedent)

t.speed("fastest")

pas = 20

for x in range(-LARGEUR_ECRAN, LARGEUR_ECRAN, pas):
  ligne(t, (0, 0), (x, -HAUTEUR_ECRAN), "blue")
  ligne(t, (0, 0), (x, HAUTEUR_ECRAN), "yellow")

for y in range(-HAUTEUR_ECRAN, HAUTEUR_ECRAN, pas):
  ligne(t, (0, 0), (-LARGEUR_ECRAN, y), "red")
  ligne(t, (0, 0), (LARGEUR_ECRAN, y), "green")

raw_input();
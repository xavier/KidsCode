import turtle

t = turtle.Pen()

def carre(t, longueur_cote):
  for i in range(4):
    t.forward(longueur_cote)
    t.left(90)

carre(t, 100)

raw_input()
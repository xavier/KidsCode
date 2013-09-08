import turtle

t = turtle.Pen()

def polygone(t, taille_cote, nombre_de_cotes):
  angle = 360.0 / nombre_de_cotes
  for i in range(0, nombre_de_cotes):
    t.forward(taille_cote)
    t.left(angle)

for n in range(3, 13):
  polygone(t, 20+(n*5), n)

raw_input()
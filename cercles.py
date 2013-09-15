import turtle

t = turtle.Pen()

def cercle(t, rayon):
  """ Dessine un cercle ayant pour centre la position actuelle de la tortue """
  t.penup()
  t.right(90)
  t.forward(rayon)
  t.left(90)
  t.pendown()
  t.circle(rayon, 360)
  t.penup()
  t.left(90)
  t.forward(rayon)
  t.right(90)
  t.pendown()

def couleur(ordre):
  teinte = (1.0/(ordre+1.25))
  return (teinte, teinte, teinte)


def cercles(t, rayon, nombre_cercles, ordre):
  t.color(couleur(ordre))
  cercle(t, rayon)
  if ordre > 0:
    distance      = rayon * 2
    nouveau_rayon = rayon / 3
    angle         = 360/nombre_cercles
    for i in range(nombre_cercles):
      t.left(angle)
      t.penup()
      t.forward(distance)
      t.pendown()
      cercles(t, nouveau_rayon, nombre_cercles, ordre-1)
      t.penup()
      t.backward(distance)
      t.pendown()

t.speed("fastest")

cercles(t, 100, 6, 3)

raw_input()
# -*- coding: UTF-8 -*-
import turtle

t = turtle.Pen()

# ½√2
FACTEUR = 0.7071067811865476

def couleur(ordre):
  teinte = (1.0/(ordre+1.5))
  return (teinte*0.5, teinte, teinte*0.5)


def arbre_de_pythagore(t, longueur_cote, ordre):
  couleur_actuelle = t.pencolor()
  t.pencolor(couleur(ordre))
  t.forward(longueur_cote)
  if ordre > 0:
    l = longueur_cote*FACTEUR
    t.right(45)
    arbre_de_pythagore(t, l, ordre-1)
    t.left(45)
  t.left(90)
  t.forward(longueur_cote)
  if ordre > 0:
    l = longueur_cote*FACTEUR
    t.right(135)
    t.penup()
    t.forward(l)
    t.pendown()
    t.left(90)
    arbre_de_pythagore(t, l, ordre-1)
    t.right(90)
    t.backward(l)
    t.left(135)
  t.left(90)
  t.forward(longueur_cote)
  t.left(90)
  t.forward(longueur_cote)
  t.left(90)
  t.pencolor(couleur_actuelle)


t.speed("fastest")

t.left(90)
arbre_de_pythagore(t, 100, 7)
t.hideturtle()

raw_input();
# -*- coding: UTF-8 -*-
import turtle
import math

t = turtle.Pen()

FACTEUR = math.sqrt(2)/2

def carre(t, longueur_cote):
  for i in range(4):
    t.forward(longueur_cote)
    t.left(90)

def carre_recursif(t, longueur_cote, n):
  carre(t, longueur_cote)
  t.forward(longueur_cote/2)
  t.left(45)
  if n > 0:
    carre_recursif(t, longueur_cote*FACTEUR, n-1)

t.speed("fast")

carre_recursif(t, 250, 10)

raw_input()
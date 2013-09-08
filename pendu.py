# -*- coding: UTF-8 -*-
from kidscode import ask
from random   import randint


mot_a_trouver = "PENDU"
lettres = []

trouve = False
essais = 5

while (not trouve) and essais > 0:
  mot_cache = ""
  for lettre in mot_a_trouver:
    if lettre in lettres:
      mot_cache += lettre
    else:
      mot_cache += "-"

  print mot_cache

  if mot_cache == mot_a_trouver:
    trouve = True
  else:
    print "Lettres:", lettres
    print "Essais: ", essais
    lettre = ask("Lettre? ").upper();
    lettres.append(lettre)
    if not lettre in mot_a_trouver:
      essais = essais - 1

print "-" * 20
if trouve:
  print "C'est gagné! :)"
else:
  print "Pendu... :("

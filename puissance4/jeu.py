# -*- coding: UTF-8 -*-

import pyssance4

print "\n!!! PUISSANCE 4 !!!\n"

grille = pyssance4.Grille()

joueur = pyssance4.JAUNE
gagne = False

while not gagne:

  print grille

  col = int(raw_input("Joueur " + joueur + ": colonne? "))

  # TODO vérifier que la paramètre colonne est correct pour éviter une exception

  ligne = grille.ajouter_pion(col, joueur)

  if grille.pion_gagnant(col, ligne):
    # Pion victorieux!
    print grille
    print "Le joureur", joueur, " a GAGNE!"
    gagne = True
  else:
    # Changement de tour
    if joueur == pyssance4.JAUNE:
      joueur = pyssance4.ROUGE
    else:
      joueur = pyssance4.JAUNE

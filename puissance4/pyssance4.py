# -*- coding: UTF-8 -*-

VIDE  = " "
ROUGE = 'R'
JAUNE = 'J'

class Erreur(Exception):
    pass

class ErreurDePosition(Erreur):
  pass

class Grille:

  """
    Grille de Puissance 4

    Le système de coordonées de la grille est compris dans l'intervalle [0;7] pour les colonnes et [0;6] pour les lignes.
    Les colonnes son numérotées de gauche à droite, les lignes sont numérotées de bas en haut.

  """

  COLONNES = 7
  LIGNES   = 6

  def __init__(self):
    self.grille = [[] for col in range(self.COLONNES)]

  def ajouter_pion(self, numero_colonne, couleur_pion):

    """ Ajoute le pion de la couleur donnée dans la colonne. Retourne la ligne à laquelle se trouve le pion ajouté """

    self.__assert_numero_colonne(numero_colonne)
    if len(self.grille[numero_colonne]) < self.LIGNES:
      self.grille[numero_colonne].append(couleur_pion)
      return len(self.grille[numero_colonne])-1
    else:
      raise Erreur("Maximum " + str(self.LIGNES) + " pions par colonne")

  def pion(self, numero_colonne, numero_ligne):

    """ Retourne la couleur du pion à la position donnée """

    self.__assert_numero_colonne(numero_colonne)
    self.__assert_numero_ligne(numero_ligne)
    colonne = self.grille[numero_colonne]
    if numero_ligne < len(colonne):
      return colonne[numero_ligne]
    else:
      return VIDE

  def pion_gagnant(self, numero_colonne, numero_ligne):

    """ Retourne True si le pion à la position indiquée fait partie d'une série de 4 """

    self.__assert_numero_colonne(numero_colonne)
    self.__assert_numero_ligne(numero_ligne)

    couleur_pion = self.pion(numero_colonne, numero_ligne)

    if couleur_pion == VIDE:
      return False

    if self.__compte_pions_de_meme_couleur_horizontalement(couleur_pion, numero_colonne, numero_ligne) > 3:
      return True
    if self.__compte_pions_de_meme_couleur_verticalement(couleur_pion, numero_colonne, numero_ligne) > 3:
      return True
    if self.__compte_pions_de_meme_couleur_diagonalement_so_ne(couleur_pion, numero_colonne, numero_ligne) > 3:
      return True
    if self.__compte_pions_de_meme_couleur_diagonalement_no_se(couleur_pion, numero_colonne, numero_ligne) > 3:
      return True

    return False

  def __str__(self):

    """ Retourne la grille formattée dans une chaîne """

    output = " " + " ".join(map(str, range(self.COLONNES)))  +"\n"
    for ligne in range(self.LIGNES, 0, -1):
      output += "|"
      for col in range(self.COLONNES):
        output += self.pion(col, ligne-1) or " "
        output += "|"
      output += "\n"
    output += "-" * ((self.COLONNES*2)+1)
    return output

  #
  # API privée
  #

  def __assert_numero_colonne(self, numero_colonne):
    if (numero_colonne < 0) or (numero_colonne >= self.COLONNES):
      raise ErreurDePosition("Le numero de colonne doit etre compris entre 0 et " + str(self.COLONNES-1))

  def __assert_numero_ligne(self, numero_ligne):
    if (numero_ligne < 0) or (numero_ligne >= self.LIGNES):
      raise ErreurDePosition("Le numero de ligne doit etre compris entre 0 et " + str(self.LIGNES-1))

  def __compte_pions_de_meme_couleur_horizontalement(self, couleur_pion, numero_colonne, numero_ligne):
    compteur_horizontal  = self.__compte_pions_de_meme_couleur(couleur_pion, numero_colonne, numero_ligne, 1, 0)
    compteur_horizontal += self.__compte_pions_de_meme_couleur(couleur_pion, numero_colonne, numero_ligne, -1, 0)-1
    return compteur_horizontal

  def __compte_pions_de_meme_couleur_verticalement(self, couleur_pion, numero_colonne, numero_ligne):
    compteur_vertical  = self.__compte_pions_de_meme_couleur(couleur_pion, numero_colonne, numero_ligne, 0, 1)
    compteur_vertical += self.__compte_pions_de_meme_couleur(couleur_pion, numero_colonne, numero_ligne, 0, -1)-1
    return compteur_vertical

  def __compte_pions_de_meme_couleur_diagonalement_so_ne(self, couleur_pion, numero_colonne, numero_ligne):
    compteur_diagonal  = self.__compte_pions_de_meme_couleur(couleur_pion, numero_colonne, numero_ligne, 1, 1)
    compteur_diagonal += self.__compte_pions_de_meme_couleur(couleur_pion, numero_colonne, numero_ligne, -1, -1)-1
    return compteur_diagonal

  def __compte_pions_de_meme_couleur_diagonalement_no_se(self, couleur_pion, numero_colonne, numero_ligne):
    compteur_diagonal  = self.__compte_pions_de_meme_couleur(couleur_pion, numero_colonne, numero_ligne, -1, 1)
    compteur_diagonal += self.__compte_pions_de_meme_couleur(couleur_pion, numero_colonne, numero_ligne, 1, -1)-1
    return compteur_diagonal

  def __compte_pions_de_meme_couleur(self, couleur_pion, numero_colonne, numero_ligne, increment_horizontal, increment_vertical):
    compteur = 0
    try:
      while (self.pion(numero_colonne, numero_ligne) == couleur_pion) and compteur < 4:
        compteur += 1
        numero_colonne += increment_horizontal
        numero_ligne += increment_vertical
    except ErreurDePosition:
      pass
    return compteur
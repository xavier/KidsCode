import codecs
import random

class Dictionnaire:

  CHEMIN_PAR_DEFAUT = "fr.dic"

  def __init__(self):
    self.mots  = []
    self.lettres = []

  def charger(self, chemin=None):

    with codecs.open(chemin or self.CHEMIN_PAR_DEFAUT, "r", "UTF-8") as fichier:
      self.mots = map(lambda mot: mot.strip(), fichier.readlines())

    lettres_uniques = set()
    for mot in self.mots:
      lettres_uniques.add(mot[:1])

    self.lettres = sorted(lettres_uniques)


  def mots_commencant_par(self, prefixe):
    return filter(lambda mot: mot.startswith(prefixe), self.mots)

  def mot_au_hasard(self, longueur_min=0, longueur_max=100):
    intervalle = xrange(longueur_min, longueur_max+1)
    return random.choice(filter(lambda mot: len(mot) in intervalle, self.mots))

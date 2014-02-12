import codecs

class Dictionnaire:

  CHEMIN_PAR_DEFAUT = "fr.dic"

  def __init__(self):
    self.mots  = []
    self.lettres = []

  def charger(self, chemin=None):

    with codecs.open(chemin or self.CHEMIN_PAR_DEFAUT, "r", "UTF-8") as fichier:
      self.mots = fichier.readlines()

    lettres_uniques = set()
    for mot in self.mots:
      lettres_uniques.add(mot[:1])

    self.lettres = sorted(lettres_uniques)


  def mots_commencant_par(self, prefixe):
    return filter(lambda mot: mot.startswith(prefixe), self.mots)
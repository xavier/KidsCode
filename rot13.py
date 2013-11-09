
def rot(chaine, cle):
  indice = 0
  resultat = ""
  while indice < len(chaine):
    car = chaine[indice]
    resultat = resultat + chr(ord(car) + cle)
    indice = indice + 1
  return resultat

def encode_rot13(chaine):
  return rot(chaine, 13)

def decode_rot13(chaine):
  return rot(chaine, -13)

secret = encode_rot13("les bonbons sont caches sous la table")
print secret
print decode_rot13(secret)

def crypte(chaine, cle):
  i = 0
  resultat = ""
  while i < len(chaine):
    resultat = resultat + chr(ord(chaine[i]) ^ cle)
    i += 1
  return resultat


chaine = "secret"
cle = 42

print crypte(chaine, cle)
print crypte(chaine, cle+1)
print crypte(crypte(chaine, cle), cle)
print crypte(crypte(chaine, cle), cle+1)
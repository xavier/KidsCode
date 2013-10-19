import coffrefort

def trouver_chiffre(position):
  chiffre = 0
  while not coffrefort.chiffre_correct(position, chiffre):
    chiffre = chiffre + 1
  return chiffre

c1 = trouver_chiffre(1)
c2 = trouver_chiffre(2)
c3 = trouver_chiffre(3)
c4 = trouver_chiffre(4)

print "code:", c1, c2, c3, c4

print "secret:", coffrefort.ouvrir(c1, c2, c3, c4)
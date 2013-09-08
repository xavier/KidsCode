# -*- coding: UTF-8 -*-
from kidscode import ask
from random   import randint

print "Devine le nombre secret entre 0 et 100!"
secret = randint(0, 100)
trouve = None
while trouve != secret:
  trouve = int(ask("? "))
  if trouve < secret:
    print "trop petit..."
  elif trouve > secret:
    print "trop grand!"
print "Gagné!"
# -*- coding: utf-8 -*-
_CODE = (3, 6, 9, 0)
SECRET = "Il y a un paquet de bonbon caché sous la table"

def chiffre_correct(position, chiffre):
	return _CODE[position-1] == chiffre

def ouvrir(c1, c2, c3, c4):
	if (c1, c2, c3, c4) == _CODE:
		return SECRET
	else:
		return None
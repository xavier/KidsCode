from datetime import datetime

def age(date_de_naissance):
  return datetime.today() - date_de_naissance

def age_en_jours(date_de_naissance):
   return age(date_de_naissance).days

def age_en_secondes(date_de_naissance):
   return age(date_de_naissance).total_seconds()

def age_en_minutes(date_de_naissance):
   return age_en_secondes(date_de_naissance) / 60

def age_en_heures(date_de_naissance):
   return age_en_minutes(date_de_naissance) / 60

def jour_naissance(date_de_naissance):
    return ("Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim")[date_de_naissance.weekday()]

date_de_naissance = datetime(1978, 7, 13)

print "Jour de naissance: ", jour_naissance(date_de_naissance)
print "Age en jours: ", age_en_jours(date_de_naissance)
print "Age en heures: ", age_en_heures(date_de_naissance)
print "Age en minutes: ", age_en_minutes(date_de_naissance)
print "Age en secondes: ", age_en_secondes(date_de_naissance)

from flask import Flask
from flask import request
from flask import session
from flask import render_template

import dictionnaire

dico = dictionnaire.Dictionnaire()
dico.charger("data/fr.dic")

app = Flask(__name__)
app.debug = True
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

def cache_lettres(mot_a_deviner, lettres_jouees):
  mot_secret = ''
  for lettre in mot_a_deviner:
    if lettre in lettres_jouees:
      mot_secret = mot_secret + lettre
    else:
      mot_secret = mot_secret + "-"
  return mot_secret

@app.route("/")
def home():
  return render_template('home.html')

@app.route("/partie", methods=['POST'])
def partie():
  mot_a_deviner  = dico.mot_au_hasard()
  lettres_jouees = ''
  erreurs = 0

  session['mot_a_deviner']  = mot_a_deviner
  session['lettres_jouees'] = lettres_jouees
  session['erreurs']        = erreurs

  mot_cache = cache_lettres(mot_a_deviner, lettres_jouees)

  return render_template('partie.html', mot_cache=mot_cache, lettres_jouees=lettres_jouees, erreurs=erreurs, gameover=False)

@app.route("/tour", methods=['GET', 'POST'])
def tour():
  lettre_proposee = request.form['lettre']

  lettres_jouees = session["lettres_jouees"]
  mot_a_deviner  = session["mot_a_deviner"]
  erreurs        = session["erreurs"]

  lettres_jouees = lettres_jouees + lettre_proposee

  if not lettre_proposee in mot_a_deviner:
    erreurs = erreurs + 1

  session['erreurs']        = erreurs
  session['lettres_jouees'] = lettres_jouees

  mot_cache = cache_lettres(mot_a_deviner, lettres_jouees)

  gameover = erreurs == 6

  return render_template('partie.html', mot_cache=mot_cache, lettres_jouees=lettres_jouees, erreurs=erreurs, gameover=gameover, mot_a_deviner=mot_a_deviner)

if __name__ == "__main__":
  app.run()
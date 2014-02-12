
from flask import Flask
from flask import request
from flask import render_template

import dictionnaire

dico = dictionnaire.Dictionnaire()
dico.charger("data/fr.dic")

app = Flask(__name__)
app.debug = True

@app.route("/")
def home_page():
  if request.args.has_key("q"):
    q = request.args.get("q")
    mots = dico.mots_commencant_par(q)
    lettre = q[:1]
  else:
    mots = []
    lettre = None
  return render_template('dico.html', lettre=lettre, lettres=dico.lettres, mots=mots)

@app.route("/mots/<prefixe>")
def mots(prefixe):
  return render_template('dico.html', lettre=prefixe[:1], lettres=dico.lettres, mots=dico.mots_commencant_par(prefixe))

if __name__ == "__main__":
  app.run()
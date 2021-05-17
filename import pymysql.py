import pymysql
from flask import render_template, Flask, request

connexion = pymysql.connect(host="mysql-joske-jones.alwaysdata.net", port=3306, user="valtaudh@gmail.com", passwd="leahugo1805", db="joske-jones_portail-badges", autocommit=True)
app = Flask(__name__)

id_utilisateur = 0
@app.route('/page_accueil')
def Accueil:
    return render_template('page_accueil_site.html')

@app.route('/page affichage utilisateurs')
def affichage:
    affichage = 'SELECT * FROM "badges"'
    return render_template('page_affichage_utilisateurs.html')

@app.route('/page modification utilisateurs')
def modification:
    if request.method == 'POST':
        nom_python = request.values["name"]
        adresse_python = request.values["address"]
        telephone_python = request.values["phone"]
        badge_python = request.values["card"]

       création = "INSERT INTO badges VALUES(NULL," + nom_python + "," + adresse_python + "," + telephone_python + "," + badge_python + ";"
       modification = "UPDATE badges SET "

if __name__ == '__main__':
    app.run(debug=True)
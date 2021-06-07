from datetime import datetime
from flask import render_template, Flask
from Projet_portail_automatique import app
import requests
import pymysql

app = Flask(__name__)

connexion = pymysql.connect(host="", port=3306, user="", passwd="leahugo1805", db="", autocommit=True)

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'page_accueil_site.html',
        title='page principale du site',
        year=datetime.now().year,
        message='bienvenue sur la page d\'accueil !'
    )

@app.route('/page affichage utilisateurs')
def affichage():
    affichage = 'SELECT * FROM "badges"'
    return render_template(
        'page_affichage_utilisateurs.html',
        title='Page affichage utilisateurs',
        year=datetime.now().year,
        message='page d\'affichage des utilisateurs'
    )

@app.route('/page modification utilisateurs')
def modification():
    if request.method == 'POST':
        nom_python = request.values["name"]
        adresse_python = request.values["address"]
        telephone_python = request.values["phone"]
        badge_python = request.values["card"]

       modification = "UPDATE badges SET" + nom_python + "," + adresse_python + "," + telephone_python + "," + badge_python + ";"
    return render_template(
        'page_modification_utilisateurs.html',
        title='page modification utilisateurs',
        year=datetime.now().year,
        message='page de modification des utilisateurs'
    )

@app.route('/page création utilisateurs')
def creation():
    if request.method =='POST':
        nom_utilisateur = request.values ['nouveau_nom_html']
        adresse_utilisateur = request.values["nouvelle_adresse_html"]
        telephone_utilisateur = request.values["nouveau_telephone_html"]
        badge_utilisateur = request.values["nouveau_badge_html"]

        creation = "INSERT INTO badges VALUES(NULL," + nom_utilisateur + "," + adresse_utilisateur + "," + telephone_utilisateur + "," + badge_utilisateur + ";"

    return render_template(
        'page_creation_utilisateurs.html',
        title='page création utilisateurs',
        year=datetime.now().year,
        message='page de création des utilisateurs'
    )
        
if __name__ == '__main__':
    app.run(debug=True)

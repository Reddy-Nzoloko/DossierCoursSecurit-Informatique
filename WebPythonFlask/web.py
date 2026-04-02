# Importation de la classe Flask et de la fonction render_template
from flask import Flask, render_template, request, redirect, url_for
from ConnexionMysql import enregistrer_utilisateur
from Dechiffrement import afficher_utilisateurs_html
# creation d'une instance de Flask
application = Flask(__name__)
# definition d'une route pour la page d'accueil
@application.route('/')
def home():
    return render_template('index.html')
# Je vais creer une route pour me ramener à la page d'enregistrement étudiant
@application.route('/enregistrement_Etudiant', methods=['GET', 'POST'])
def enregistrement_etudiant():
    if request.method == 'POST':
        # traitement des données du formulaire d'enregistrement
        nom = request.form['nom']
        postnom = request.form['postnom']
        email = request.form['email']
        # Ici, vous pouvez ajouter le code pour traiter les données du formulaire d'enregistrement
        # Enregistrement chiffré des informations de l'utilisateur dans la base de données
        enregistrer_utilisateur(nom, postnom, email)
        return redirect(url_for('home'))
    else:
        return render_template('enregistrement_Etudiant.html')
    
# Affichage des utilisateurs de la base de données dans un formulaire html pour que je puisse les afficher dans mon application web flask
@application.route('/afficher_Etudiant')
def afficher_utilisateurs():
    utilisateurs = afficher_utilisateurs_html()
    return render_template('afficher_Etudiant.html', utilisateurs=utilisateurs)

# Affichage unique d'un utilisateur et modification de ses informations
@application.route('/liste_etudiants')
def etudiants():
    resultat=afficher()
    return render_template('etudiants.html',etudiants=resultat)

@application.route('/modifier/<id>',methods=['GET','POST'])
def modifier_etudiant(email):
    if request.method == 'POST':
        nom=request.form.get('nom')
        postnom=request.form.get('postnom')
        modifier(email,nom,postnom)
        return redirect(url_for('etudiants'))
    else:
        etudiant=afficher_etudiant_unique(email)
        return render_template('modifier.html',etudiant=etudiant)
    # return render_template('enregistrement_Etudiant.html')
# lancement de notre application Flask
if __name__ == '__main__':
    application.run(debug=True, port=5001)
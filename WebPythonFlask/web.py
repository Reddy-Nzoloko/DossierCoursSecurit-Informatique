# Importation de la classe Flask et de la fonction render_template
from flask import Flask, render_template, request, redirect, url_for
from ConnexionMysql import enregistrer_utilisateur
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

    # return render_template('enregistrement_Etudiant.html')
# lancement de notre application Flask
if __name__ == '__main__':
    application.run(debug=True, port=5001)
from flask import Flask,render_template,request,redirect,url_for
from exercice1 import enregistrer_utilisateur,afficher,afficher_etudiant_unique,modifier
#creation d'une instance de Flask
application=Flask(__name__)
#definition des routes et des fonctions(vues)
@application.route('/')
def home():
    return render_template('index.html')

@application.route('/enregistrer',methods=['GET','POST'])
def enregistrer_etudiant():
    if request.method == 'POST':
        #traitement du formulaire
        nom=request.form.get("nom")
        postnom=request.form.get("postnom")
        email=request.form.get("email")
        #enregistrer utilisateur
        enregistrer_utilisateur(nom,postnom,email)

        return redirect(url_for('etudiants'))
    else:
        
        return render_template('form_etudiant.html')

@application.route('/liste_etudiants')
def etudiants():
    resultat=afficher()
    return render_template('etudiants.html',etudiants=resultat)

@application.route('/modifier/<email>',methods=['GET','POST'])
def modifier_etudiant(email):
    if request.method == 'POST':
        nom=request.form.get('nom')
        postnom=request.form.get('postnom')
        modifier(email,nom,postnom)
        return redirect(url_for('etudiants'))
    else:
        etudiant=afficher_etudiant_unique(email)
        return render_template('modifier.html',etudiant=etudiant)

#lancement de notre application
if __name__=='__main__':
    application.run(debug=True)
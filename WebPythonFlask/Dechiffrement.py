#import de la bibliotheque mysql.connector
import mysql.connector
from cryptography.fernet import Fernet
import os

#on se connecte a la base de donnees mysql
def connect():
    bd = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="SecuriteInformatique"
        )
    return bd
#creation d'un curseur pour executer les requetes sql
curseur = connect().cursor()
#fonnction pour dechiffrees les donnees deja chiffrees dispo dans la bdd
def dechiffrer_message(message_chiffre):
    #recuperation de la cle a partir du variable d'environnement que j'ai nommee Fernet
    cle=os.environ.get("Fernet")
    if cle is None:
        raise ValueError("The 'Fernet' environment variable is not set. Please set it before running this script.")
    #on charge le chiffrement
    chiffrement=Fernet(cle.encode())
    #dechiffrement du message
    message_dechiffre = chiffrement.decrypt(message_chiffre).decode()
    return message_dechiffre

#recuperation et affichage des donnees de la base de donnees
def afficher_utilisateurs():
    bd = connect()
    curseur = bd.cursor()
    requete = "SELECT nom, postnom, email FROM utilisateur"
    curseur.execute(requete)
    utilisateurs = curseur.fetchall()
    for utilisateur in utilisateurs:
        nom_dechiffre = dechiffrer_message(utilisateur[0])
        postnom_dechiffre = dechiffrer_message(utilisateur[1])
        email_dechiffre = dechiffrer_message(utilisateur[2])
        # print(f"nom: {nom_dechiffre}, Postnom: {postnom_dechiffre}, Email: {email_dechiffre}")
    curseur.close()
    bd.close()

# print(f"Utilisateurs dans la base de données :")
afficher_utilisateurs()

# je vais creer une fonction qui va me permettre d'afficher les utilisateurs de la base de donnée dans un formulaire html pour que je puisse les afficher dans mon application web flask
def afficher_utilisateurs_html():
    bd = connect()
    curseur = bd.cursor()
    requete = "SELECT nom, postnom, email FROM utilisateur"
    curseur.execute(requete)
    utilisateurs = curseur.fetchall()
    utilisateurs_dechiffres = []
    for utilisateur in utilisateurs:
        nom_dechiffre = dechiffrer_message(utilisateur[0])
        postnom_dechiffre = dechiffrer_message(utilisateur[1])
        email_dechiffre = dechiffrer_message(utilisateur[2])
        utilisateurs_dechiffres.append((nom_dechiffre, postnom_dechiffre, email_dechiffre))
    curseur.close()
    bd.close()
    #return utilisateurs_dechiffres

    # Affichage unique d'un utilisateur
def afficher_etudiant_unique(id):
    enregistrement={}
    requete="SELECT * FROM utilisateur WHERE id=%s"
    bd = connect()
    curseur = bd.cursor()
    valeur=(id,)
    curseur.execute(requete,valeur)
    resultat=curseur.fetchall()
    for r in resultat:
        nom= dechiffrer_message(r[1])
        postnom= dechiffrer_message(r[2])
        email= dechiffrer_message(r[3])
        id=r[0] 
        enregistrement={"nom":nom.decode(),"postnom":postnom.decode(),"email":email.decode(), "id":id}
    return enregistrement

# fonction pour la modification 
def modifier(id,email,nom,postnom):
    requete="UPDATE utilisateur SET nom=%s,postnom=%s, email=%s WHERE id=%s"
    bd = connect()
    curseur = bd.cursor()
    nom=dechiffrer_message(nom)
    postnom=dechiffrer_message(postnom)
    email=dechiffrer_message(email)
    valeur=(id,nom,postnom,email,)
    curseur.execute(requete,valeur)
    bd.commit()
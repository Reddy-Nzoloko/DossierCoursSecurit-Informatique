from cryptography.fernet import Fernet
import mysql.connector
import os
def connecter():
    #on se connecte a la base de donnees
    bd=mysql.connector.connect(
        database='bdsecurite',
        host='localhost',
        user='root',
        password=''
    )
    #on cree le curseur dont le role est d'executer
    # les requetes sql
    
    return bd

def chiffrer(message_clair):
    #Recuperation de la cle a partir de la variable
    #d'environnement
    cle=os.environ.get('FERNET_KEY')
    #on charge le chiffrement
    chiffrement=Fernet(cle.encode())
    #on chiffre le message clair
    message_chiffre=chiffrement.encrypt(message_clair.encode())
    return message_chiffre

def enregistrer_utilisateur(nom,postnom,email):
    #requete d'insertion
    requete="INSERT INTO utilisateur VALUES (%s,%s,%s)"
    #chiffrement
    nom=chiffrer(nom)
    postnom=chiffrer(postnom)
    #email=chiffrer(email)
    valeurs=(email,nom,postnom)
    #connexion
    bd=connecter()
    #curseur pour executer la requete sql

    curseur=bd.cursor()
    #on execute la requete sql par le curseur
    curseur.execute(requete,valeurs)

    bd.commit()

    return "Enregistrement reussi"

    
    pass
def dechiffrer(message):
    cle=os.environ.get('FERNET_KEY')
    dechiffrement=Fernet(cle)
    message_clair=dechiffrement.decrypt(message)
    return message_clair

def afficher():
    liste_etudiants=[]
    requete="SELECT * FROM utilisateur"
    db=connecter()
    curseur=db.cursor()
    curseur.execute(requete)
    etudiants=curseur.fetchall()
    for et in etudiants:
        nom=dechiffrer(et[1])
        postnom=dechiffrer(et[2])
        email=et[0]
        liste_etudiants.append({"nom":nom.decode(),"postnom":postnom.decode(),"email":email})
    return liste_etudiants
def afficher_etudiant_unique(email):
    enregistrement={}
    requete="SELECT * FROM utilisateur WHERE email=%s"
    db=connecter()
    curseur=db.cursor()
    valeur=(email,)
    curseur.execute(requete,valeur)
    resultat=curseur.fetchall()
    for r in resultat:
        nom=dechiffrer(r[1])
        postnom=dechiffrer(r[2])
        email=r[0]
        enregistrement={"nom":nom.decode(),"postnom":postnom.decode(),"email":email}
    return enregistrement

def modifier(email,nom,postnom):
    requete="UPDATE utilisateur SET nom=%s,postnom=%s WHERE email=%s"
    db=connecter()
    curseur=db.cursor()
    nom=chiffrer(nom)
    postnom=chiffrer(postnom)
    valeur=(nom,postnom,email,)
    curseur.execute(requete,valeur)
    db.commit()

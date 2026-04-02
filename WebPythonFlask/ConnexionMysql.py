# Connexion à la base de donnée mysql et cryptage de message avant de l'insérer dans la base de donnée
# Importation des bibliothèques nécessaires
import mysql.connector
from cryptography.fernet import Fernet
import os

# on se connecte à notre base de donnée mysql qui est nommé SecuriteInformatique par une fonction
def connecter():
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="SecuriteInformatique"
    )
    # on creer le cursor pour executer les requetes sql
    curseur = connexion.cursor()
    return curseur, connexion



# On creer la fonction qui va nous permettre d'utiliser notre variable d'environnement pour la clé de chiffrement
def chiffrer_message(message_claire):
    # on recupere la clé de chiffrement depuis la variable d'environnement
    cle = os.environ.get("Fernet")
    # on creer un objet Fernet avec la clé de chiffrement
    chiffrement = Fernet(cle.encode())
    # on chiffre le message claire
    message_chiffre = chiffrement.encrypt(message_claire.encode())  
    return message_chiffre


def enregistrer_utilisateur(nom, postNom, email):
    requete = "INSERT INTO utilisateur (nom, postNom, email) VALUES (%s, %s, %s)"
    # chiffrement du message claire
    nom = chiffrer_message(nom)
    postNom = chiffrer_message(postNom)
    email = chiffrer_message(email)   
    valeurs=(nom, postNom, email)
    # curseur pour executer la requete sql   
    curseur, connexion = connecter()
    curseur.execute(requete, valeurs)
    print("Utilisateur enregistré avec succès !")
    connexion.commit()
    connexion.close()

# Maintenant je vais tester la fonction enregistrer_utilisateur pour voir si elle fonctionne correctement
# enregistrer_utilisateur("Reddy", "Nzoloko", "reddynzoloko@gmail.com")

# affichage Unique d'un

# on travail pour chiffrement symetrique 
from cryptography.fernet import Fernet

message_claire = "Bonjour, comment allez-vous ?"
# generation de la cle de chiffrement
cle_de_chiffrement = Fernet.generate_key()
# Je vais afficher la clé
print("Clé de chiffrement :", cle_de_chiffrement.decode())
# creation d'un objet Fernet avec la cle de chiffrement
chiffrement = Fernet(cle_de_chiffrement)
# chiffrement du message claire
message_chiffre = chiffrement.encrypt(message_claire.encode())   
print("Message claire :", message_claire)
print("Message chiffre :", message_chiffre)

# dechiffrement du message chiffre
message_dechiffre = chiffrement.decrypt(message_chiffre).decode()
print("Message dechiffre :", message_dechiffre)


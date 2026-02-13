from random import *
from time import sleep
import fonctions
from classes import *

Couleurs = ["H", "D", "C", "S"]
Cartes = []
for C in Couleurs :
    for V in range(2,15) :
        carte = Carte(V, C)
        Cartes.append(carte)









Listejoueurs=[]

banque_depart = 0
while True :
    Banque=input("Banque de départ ? ")
    try:
        Banque=int(Banque)
    except:
        print("Entrez un nombre superieur ou égal à 100")
    else:
        if Banque<100:
            print("Entrez un nombre superieur ou égal à 100 ")
        else:
            banque_depart = Banque
            break

while True :
    nbj=input("Nombre de joueurs ? ")
    try:
        nbj=int(nbj)
    except:
        print("Entrer un nombre compris entre 2 et 9")
    else:
        if nbj>1 and nbj <=9:
            for i in range(nbj):
                joueur = Joueur("",i,banque_depart)
                Listejoueurs.append(joueur)
            break
        else:
            print("Entrer un nombre compris entre 2 et 9")


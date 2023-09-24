from random import *

J11=""
J12=""
J21=""
J22=""
J31=""
J32=""
J41=""
J42=""
J51=""
J52=""
J61=""
J62=""
J71=""
J72=""
J81=""
J82=""
J91=""
J92=""

ListeCartes = ['Ah','2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'Jh', 'Qh', 'Kh', 'Ac','2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'Jc', 'Qc', 'Kc', 'Ad','2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'Jd', 'Qd', 'Kd', 'As','2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'Js', 'Qs', 'Ks',]
DJoueurs = {"J1":[J11,J12],"J2":[J21,J22],"J3":[J31,J32],"J4":[J41,J42],"J5":[J51,J52],"J6":[J61,J62],"J7":[J71,J72],"J8":[J81,J82],"J9":[J91,J92]}


Cartes=ListeCartes.copy()
Joueurs=DJoueurs.copy()

nbj=int(input("Nombre de joueurs ? "))

nbjok=False                              #Initialise le nombre de joueurs
while not nbjok:                         #tant qu'il est entre 2 et 9
    if nbj>1 and nbj <9:
        Joueurs=Joueurs[:nbj]
        nbjok=True
    elif nbj==9:
        nbjok=True
    else:
        print("Entre deux joueurs minimum et 9 joueurs maximum requis")
        nbj=int(input("Nombre de joueurs ?"))


for i in Joueurs.keys():
    Joueurs[i][0] = Cartes.pop(randint(0,len(Cartes))) # Joueur 1 Carte 1
    Joueurs[i][1] = Cartes.pop(randint(0,len(Cartes))) # Joueur 2 Carte 2

print(Joueurs[1][0])          # Vérifications
print(Joueurs[1][1])
print(J21)          
print(J22)

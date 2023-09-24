from random import *
from time import sleep
import fonctions

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

M1=[]
M2=[]
M3=[]
M4=[]
M5=[]
M6=[]
M7=[]
M8=[]
M9=[]
 
ListeCartes = ['Ah','2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 'Kh', 'Ac','2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 'Jc', 'Qc', 'Kc', 'Ad','2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 'Td', 'Jd', 'Qd', 'Kd', 'As','2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'Ts', 'Js', 'Qs', 'Ks',]
DJoueurs = {"J1":[J11,J12],"J2":[J21,J22],"J3":[J31,J32],"J4":[J41,J42],"J5":[J51,J52],"J6":[J61,J62],"J7":[J71,J72],"J8":[J81,J82],"J9":[J91,J92]}
Listemains=[M1,M2,M3,M4,M5,M6,M7,M8,M9]

Cartes=ListeCartes.copy()
Joueurs={}

nbj=int(input("Nombre de joueurs ? "))
print()

nbjok=False
listtemp=list(DJoueurs.keys())                              #Initialise le nombre de joueurs
while not nbjok:                         #tant qu'il est entre 2 et 9
    if nbj>1 and nbj <9:
        for i in range(nbj):
            Joueurs[listtemp[i]]=DJoueurs[listtemp[i]]
        Listemains=Listemains[:nbj]
        nbjok=True
    elif nbj==9:
        nbjok=True
        for i in range(nbj):
            Joueurs[listtemp[i]]=DJoueurs[listtemp[i]]
    else:
        print("Entre deux joueurs minimum et 9 joueurs maximum requis")
        nbj=int(input("Nombre de joueurs ?"))

nbjv = nbj                            # Initialise le nombre de joueur au début d'une partie (Nombre de joueurs en vie)
#while nbjv < 1:
nbjs = nbjv                       # Initialise le nombre de joueur qui suivent la main
for i in Joueurs.keys():
    Joueurs[i][0] = Cartes.pop(randint(0,len(Cartes)-1)) # Joueur 1 Carte 1
    Joueurs[i][1] = Cartes.pop(randint(0,len(Cartes)-1)) # Joueur 2 Carte 2
    print(i,Joueurs[i][0],Joueurs[i][1])
    
print()

#Flop
#while nbjs>1:
F1 = Cartes.pop(randint(0,len(Cartes)-1)) # Oh mais c'est gênant ! Quoicouflop
F2 = Cartes.pop(randint(0,len(Cartes)-1))
F3 = Cartes.pop(randint(0,len(Cartes)-1))
F4 = Cartes.pop(randint(0,len(Cartes)-1))
F5 = Cartes.pop(randint(0,len(Cartes)-1))
print(F1,F2,F3,F4,F5)

templist=list(Joueurs.keys())
for i in range(len(Listemains)):
    #Listemains[i]=F1+F2+F3+F4+F5+Joueurs[templist[i][0]]+Joueurs[templist[i][1]]
    Listemains[i].append(F1)
    Listemains[i].append(F2)
    Listemains[i].append(F3)
    Listemains[i].append(F4)
    Listemains[i].append(F5)
    Listemains[i].append(Joueurs[templist[i]][0])
    Listemains[i].append(Joueurs[templist[i]][1])
    print(i+1,":",Listemains[i])
    
print(fonctions.quinte(M1))
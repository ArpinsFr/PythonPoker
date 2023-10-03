from random import *
from time import sleep
import fonctions

nbjv=9

while nbjv>1 :

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

  C1=[]
  Q1=[]
  Fl1=[]
  C2=[]
  Q2=[]
  Fl2=[]
  C3=[]
  Q3=[]
  Fl3=[]
  C4=[]
  Q4=[]
  Fl4=[]
  C5=[]
  Q5=[]
  Fl5=[]
  C6=[]
  Q6=[]
  Fl6=[]
  C7=[]
  Q7=[]
  Fl7=[]
  C8=[]
  Q8=[]
  Fl8=[]
  C9=[]
  Q9=[]
  Fl9=[]
  
  Scores = []
  Valeurs = [] 
  CartesH = []

  
  ListeCartes = ['Ah','2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 'Kh', 'Ac','2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 'Jc', 'Qc', 'Kc', 'Ad','2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 'Td', 'Jd', 'Qd', 'Kd', 'As','2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'Ts', 'Js', 'Qs', 'Ks',]
  DJoueurs = {"J1":[J11,J12],"J2":[J21,J22],"J3":[J31,J32],"J4":[J41,J42],"J5":[J51,J52],"J6":[J61,J62],"J7":[J71,J72],"J8":[J81,J82],"J9":[J91,J92]}
  Listemains=[M1,M2,M3,M4,M5,M6,M7,M8,M9]
  Checkmain=[[C1,Q1,Fl1],[C2,Q2,Fl2],[C3,Q3,Fl3],[C4,Q4,Fl4],[C5,Q5,Fl5],[C6,Q6,Fl6],[C7,Q7,Fl7],[C8,Q8,Fl8],[C9,Q9,Fl9]]
  Cartes=ListeCartes.copy()
  Joueurs={}
  
  print()
  
  nbjok=False
  listtemp=list(DJoueurs.keys())                              #Choix + Initialisation du nombre de joueurs
  while not nbjok:
      nbj=input("Nombre de joueurs ? ")
      try:
          nbj=int(nbj)
      except:
          print("Entrer un nombre compris entre 2 et 9")
      else:
          if nbj>1 and nbj <=9:
              for i in range(nbj):
                  Joueurs[listtemp[i]]=DJoueurs[listtemp[i]]
              Listemains=Listemains[:nbj]
              nbjok=True
          else:
              print("Entrer un nombre compris entre 2 et 9")
  
  nbjv = nbj                            # Initialise le nombre de joueur au début d'une partie (Nombre de joueurs en vie)
  
  #while nbjv < 1:  --->  Lui il est bien placé on s'en servira que à la fin pour faire les boucles
  
  nbjs = nbjv                       # Initialise le nombre de joueur qui suivent la main
  for i in Joueurs.keys():
      Joueurs[i][0] = Cartes.pop(randint(0,len(Cartes)-1)) # Joueur 1 Carte 1
      Joueurs[i][1] = Cartes.pop(randint(0,len(Cartes)-1)) # Joueur 2 Carte 2
      print(i,Joueurs[i][0],Joueurs[i][1])
      
  print()
  
  #Flop
  
  #while nbjs>1: ---> Je sais pas ce que tu veux en faire mais ça va tirer des cartes à l'infini là ---> pas d'utilité tant que pas de mise
  
  F1 = Cartes.pop(randint(0,len(Cartes)-1)) # Oh mais c'est gênant ! Quoicouflop
  F2 = Cartes.pop(randint(0,len(Cartes)-1))
  F3 = Cartes.pop(randint(0,len(Cartes)-1))
  
  #On est censé mettre un truc ici pour les mises
  
  F4 = Cartes.pop(randint(0,len(Cartes)-1))
  
  # Ici aussi
  
  F5 = Cartes.pop(randint(0,len(Cartes)-1))
  print(F1,F2,F3,F4,F5)
  
  templist=list(Joueurs.keys())                   #Donne pour chaque joueur sa main totale ( 7 cartes )
  for i in range(len(Listemains)):
      Listemains[i].append(F1)
      Listemains[i].append(F2)
      Listemains[i].append(F3)
      Listemains[i].append(F4)
      Listemains[i].append(F5)
      Listemains[i].append(Joueurs[templist[i]][0])
      Listemains[i].append(Joueurs[templist[i]][1])
  
  for i in range (nbj):                           # DEBUG --- Affiche les mains totales de chaque joueurs + les combinaisons 
    print("\n","JOUEUR",i+1,"\n")
    print(Listemains[i])
    Checkmain[i][0]=fonctions.check(Listemains[i]).copy()
    print(fonctions.check(Listemains[i]))
    Checkmain[i][1]=fonctions.quinte(Listemains[i])
    print("Quinte :",fonctions.quinte(Listemains[i]))
    Checkmain[i][2]=fonctions.flush(Listemains[i]).copy()
    print("Flush :",fonctions.flush(Listemains[i]))

  print(Checkmain[2][0])
  print(Checkmain[2][1])
  print(Checkmain[2][2])
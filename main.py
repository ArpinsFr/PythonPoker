from random import *
from time import sleep
import fonctions

nbjv=9

while nbjv>1 :
  Scores = []
  Valeurs = [] 
  CartesH = []

  
  Cartes = ['Ah','2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 'Kh', 'Ac','2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 'Jc', 'Qc', 'Kc', 'Ad','2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 'Td', 'Jd', 'Qd', 'Kd', 'As','2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'Ts', 'Js', 'Qs', 'Ks']
  DJoueurs = {"J1":[0,0],"J2":[0,0],"J3":[0,0],"J4":[0,0],"J5":[0,0],"J6":[0,0],"J7":[0,0],"J8":[0,0],"J9":[0,0]}
  Listemains=[[],[],[],[],[],[],[],[],[]]
  Points=[0,0,0,0,0,0,0,0,0]
  Checkmain=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
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
  
  #while nbjv > 1:  --->  Lui il est bien placé on s'en servira que à la fin pour faire les boucles
  
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

  print()
  print()
  
  for i in range(nbj):
    if Checkmain[i][2][0]=='QF':
      Listemains[i]=Checkmain[i][2]
      Points[i]=8
    elif Checkmain[i][0][0]=='Carre' or Checkmain[i][0][0]=='Full':
      Listemains[i]=Checkmain[i][0]
      if Checkmain[i][0][0]=='Carre':
        Points[i]=7
      else:
        Points[i]=6
    elif Checkmain[i][2][0]=='F':
      Listemains[i]=Checkmain[i][2]
      Points[i]=5
    elif Checkmain[i][1][0]=='Q':
      Listemains[i]=Checkmain[i][1]
      Points[i]=4
    else:
      Listemains[i]=Checkmain[i][0]
      if Checkmain[i][0][0]=='Brelan':
        Points[i]=3
      elif Checkmain[i][0][0]=='DPaire':
        Points[i]=2
      elif Checkmain[i][0][0]=='Paire':
        Points[i]=1
    print(Listemains[i])

  indl=[]
  m=Points[0]
  for i in range(nbj):
    if Points[i]>m:
      m=Points[i]
      indl=[i]
    elif Points[i]==m:
      indl.append(i)
  print()
  print(indl)

  win=fonctions.comparer(indl,Listemains,len(Listemains[indl[0]]))
  try:
    a=win[0]
  except:
    if Listemains[win][1]==14:
      card="As"
    elif Listemains[win][1]==13:
      card="Roi"
    elif Listemains[win][1]==12:
      card="Dame"
    elif Listemains[win][1]==11:
      card="Valet"
    else:
      card=Listemains[win][1]
    if Listemains[win][0]=="Full":
      if Listemains[win][2]==14:
        card2="As"
      elif Listemains[win][2]==13:
        card2="Roi"
      elif Listemains[win][2]==12:
        card2="Dame"
      elif Listemains[win][2]==11:
        card2="Valet"
      else:
        card2=Listemains[win][2]
      print("Le joueur",win+1,"gagne avec un full aux",card,"par les",card2)
    elif Listemains[win][0]=="DPaire":
      if Listemains[win][2]==14:
        card2="As"
      elif Listemains[win][2]==13:
        card2="Roi"
      elif Listemains[win][2]==12:
        card2="Dame"
      elif Listemains[win][2]==11:
        card2="Valet"
      else:
        card2=Listemains[win][2]
      print("Le joueur",win+1,"gagne avec une double paire de",card,"et de",card2)
    elif Listemains[win][0]=="F":
      print("Le joueur",win+1,"gagne avec une Flush")
    else:
      if Listemains[win][0]=="QF":
        main="Quinte Flush"
      elif Listemains[win][0]=="Q":
        main="Quinte"
      else:
        main=Listemains[win][0]
      print("Le joueur",win+1,"gagne avec une",main,"de",card)
  else:
    egal="Egalité entre les joueurs "
    for i in win:
      egal = egal + str(i+1)
      if i != win[-1]:
        egal = egal + " et "
    print(egal)
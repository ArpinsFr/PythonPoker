from random import *
from time import sleep
import fonctions

GBlinde = 0
PBlinde = 0
def tour(tour,nbjs):
  if nbjs>2:
    if tour==nbjs-2:
      tmise=0
    elif tour>=nbjs-1:
      tmise=1
    else:
      tmise=tour+2
  else:
    if tour>1:
      tmise=1
    else:
      tmise=tour
  return(tmise)

def printmain(i) :
  global Checkmain,JoueursSuivent
  if Checkmain[JoueursSuivent[i]][2][0]=='QF' :
    print("-- Quinte Flush --")
  elif Checkmain[JoueursSuivent[i]][0][0] == "Carre" :
    print("-- Carre --")
  elif Checkmain[JoueursSuivent[i]][0][0] == "Full" :
    print("-- Full --")
  elif Checkmain[JoueursSuivent[i]][2][0]=='F' :
    print("-- Couleur --")
  elif Checkmain[JoueursSuivent[i]][1][0]=='Q' :
    print("-- Quinte --")
  elif Checkmain[JoueursSuivent[i]][0][0] == 'Brelan' :
    print('-- Brelan --')
  elif Checkmain[JoueursSuivent[i]][0][0] == 'DPaire' :
    print('-- Double Paire --')
  elif Checkmain[JoueursSuivent[i]][0][0] == 'Paire' :
    print('-- Paire --')
  else:
    print('-- Carte Haute --')

def suivre(mise,tmise,nbjs):
  if nbjs>1:
    global F1,F2,F3,F4,F5,GBlinde,Banques,JoueursSuivent,Mises,Pot,JTapis
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n","Cartes milieu :",flop)
    sleep(2)
    tmise=tour(tmise,nbjs)
    attribuemain()
    for i in range(nbjs):
        if i not in JTapis:
          print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
          print("Joueur",JoueursSuivent[tmise]+1,"\n")
          print("Main actuelle :",Listemains[JoueursSuivent[tmise]])
          if len(Listemains[JoueursSuivent[tmise]])>2:
            printmain(tmise)
          print("Banque :",Banques[JoueursSuivent[tmise]])
          print("Mise actuelle :",mise,"\n")
          tok=False
          if mise==0:
            while not tok :
              print("Check / Miser / Se Coucher")
              a=input("C / M / F\n")
              if a=="C":
                tok=True
              elif a=="M":
                miseok=False
                while True :
                  b=input("Mise ? (Minimum : "+str(GBlinde)+" )\n")
                  try:
                    b=int(b)
                  except:
                    pass
                  else: 
                    if b>=GBlinde:
                      if b>Banques[JoueursSuivent[tmise]]:
                        print("Pas assez d'argent")
                      if b==Banques[JoueursSuivent[tmise]]:
                        tapisok=input("Tapis ? (O/N)")
                        if tapisok=="O" :
                          Pot+=Banques[JoueursSuivent[tmise]]
                          Banques[JoueursSuivent[tmise]]=0
                          mise=b
                          JTapis.append(JoueursSuivent[tmise])
                          tok=True
                          return["R",tmise,mise]
                      else:
                        Banques[JoueursSuivent[tmise]]-=b
                        Pot=Pot+(b-Mises[JoueursSuivent[tmise]])
                        mise=b
                        Mises[JoueursSuivent[tmise]]=b
                        return(["R",tmise,mise])
              elif a=="F":
                JoueursSuivent[tmise]="Fold"
                tok=True
          if tmise==nbjs-1:
            tmise=0
          else:
           tmise+=1
    return[0]
  else:
    suiviok=True
def suivre2(mise,tmise,nbjs):
    global F1,F2,F3,F4,F5,GBlinde,Banques,JoueursSuivent,Mises,Pot,Listemains,JTapis
    tmise=tour(tmise,nbjs)
    attribuemain()
    for i in range(nbjs-1):
      if JoueursSuivent[tmise] not in JTapis:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("Joueur",JoueursSuivent[tmise]+1,"\n")
        print("Main actuelle :",Listemains[JoueursSuivent[tmise]])
        if len(Listemains[JoueursSuivent[tmise]])>2:
          printmain(tmise)
        print("Banque :",Banques[JoueursSuivent[tmise]])
        print("Mise actuelle :",mise,"\n")
        tok=False
        while not tok:
          if mise >= Banques[JoueursSuivent[tmise]]:
            print("Tapis (",Banques[JoueursSuivent[tmise]],") / Se Coucher")
            a=input("T / F")
          else :
            print("Suivre (",(mise-Mises[JoueursSuivent[tmise]]),") / Relancer (Minimum :",2*mise,") / Se Coucher")
            a=input("S / R / F\n")
          if a=="S":
            tok=True
            Banques[JoueursSuivent[tmise]]-=(mise-Mises[JoueursSuivent[tmise]])
            Pot=Pot+(mise-Mises[JoueursSuivent[tmise]])
            Mises[JoueursSuivent[tmise]]=mise
          elif a=="R":
            miseok=False
            while not miseok:
              b=input("Mise ? (Minimum : "+str(2*mise)+" )\n")
              try:
                b=int(b)
              except:
                pass
              else: 
                if b>2*mise :
                  if b>Banques[JoueursSuivent[tmise]]:
                    print("Pas assez d'argent")
                  else:
                    Banques[JoueursSuivent[tmise]]-=(b-Mises[JoueursSuivent[tmise]])
                    Pot+=(b-Mises[JoueursSuivent[tmise]])
                    Mises[JoueursSuivent[tmise]]=b
                    mise=b
                    tok=True
                    miseok=True
                    return(["R",tmise,mise])  
                elif b==Banques[JoueursSuivent[tmise]]:
                  tapisok=input("Tapis ? (O/N)")
                  if tapisok=="O" :
                    Pot+=Banques[JoueursSuivent[tmise]]
                    Banques[JoueursSuivent[tmise]]=0
                    JTapis.append(JoueursSuivent[tmise])
                    tok=True
                    mise=b
                    miseok=True

          elif a=="F":
            JoueursSuivent[tmise]="Fold"
            tok=True
          elif a=="T":
            tok=True
            Pot=Pot+Banques[JoueursSuivent[tmise]]
            Banques[JoueursSuivent[tmise]]=0
            JTapis.append(JoueursSuivent[tmise])
        if tmise==nbjs-1:
          tmise=0
        else:
          tmise+=1
    return[0] 
  
def fold():
  global JoueursSuivent,nbjs
  i=0
  while i<nbjs:
    if JoueursSuivent[i] == "Fold":
      nbjs-=1
      JoueursSuivent.pop(i)
    else:
      i+=1

def attribuemain():
  global Checkmain,JoueursSuivent,nbjs
  for i in range (nbjs):    
    print("\n","JOUEUR",i+1,"\n")
    print(Listemains[i])
    Checkmain[JoueursSuivent[i]][0]=fonctions.check(Listemains[JoueursSuivent[i]])
    Checkmain[JoueursSuivent[i]][1]=fonctions.quinte(Listemains[JoueursSuivent[i]])
    Checkmain[JoueursSuivent[i]][2]=fonctions.flush(Listemains[JoueursSuivent[i]])
    
DeJoueurs = {"J1":[0,0],"J2":[0,0],"J3":[0,0],"J4":[0,0],"J5":[0,0],"J6":[0,0],"J7":[0,0],"J8":[0,0],"J9":[0,0]}
Joueurs2={}
Listemains2=[[],[],[],[],[],[],[],[],[]]
Banques=[0,0,0,0,0,0,0,0,0]
Listejoueurs=[]
Mises = []
nbjok=False
listtemp=list(DeJoueurs.keys())                              #Choix + Initialisation du nombre de joueurs
while not nbjok:
    nbj=input("Nombre de joueurs ? ")
    try:
        nbj=int(nbj)
    except:
        print("Entrer un nombre compris entre 2 et 9")
    else:
        if nbj>1 and nbj <=9:
            for i in range(nbj):
                Joueurs2[listtemp[i]]=DeJoueurs[listtemp[i]]
                Listejoueurs.append(i)
            Listemains2=Listemains2[:nbj]
            nbjok=True
        else:
            print("Entrer un nombre compris entre 2 et 9")

bank=False
while not bank:
  Banque=input("Banque de départ ? ")
  try:
    Banque=int(Banque)
  except:
    print("Entrez un nombre superieur ou égal à 100")
  else:
    if Banque<100:
      print("Entrez un nombre superieur ou égal à 100 ")
    else:
      for k in range(nbj):
        Banques[k]=Banque
      bank=True
blind=False
while not blind:
  PBlinde=input("Valeur de la blinde ? ")
  try:
    PBlinde=int(PBlinde)
  except:
    print("Entrez un nombre entre 10 et",Banque//2)
  else:
    if PBlinde>Banque//2 or PBlinde<10:
      print("Entrez un nombre entre 10 et",Banque//2)
    else:
      GBlinde = 2 * PBlinde
      blind=True
      
for i in range(nbj):
  Mises.append(0)
nbjv = nbj


Tour = 0 #Nombre du tour, permet de définir qui paye la blinde


while nbjv>1 :
  JTapis=[]
  Scores = []
  Valeurs = [] 
  CartesH = []
  Pot=0
  JoueursSuivent = Listejoueurs.copy()
  MiseMax = GBlinde
  flop=[]
  Cartes = ['Ah','2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 'Kh', 'Ac','2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 'Jc', 'Qc', 'Kc', 'Ad','2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 'Td', 'Jd', 'Qd', 'Kd', 'As','2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'Ts', 'Js', 'Qs', 'Ks']
  DJoueurs = DeJoueurs.copy()
  Listemains=Listemains2.copy()
  Points=[0,0,0,0,0,0,0,0,0]
  Checkmain=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
  Joueurs=Joueurs2.copy()
  print()
  for i in range (nbjv):
    Listemains[i]=[]
    Mises[i]=0
  input("Appuyez pour commencer le tour")
  
  nbjs = nbjv                       # Initialise le nombre de joueur qui suivent la main
  if Tour == nbjv-1:
    Banques[Tour]-=PBlinde
    Mises[Tour]=PBlinde
    Banques[0]-=GBlinde
    Mises[0]=GBlinde
  else:
    Banques[Tour]-=PBlinde
    Mises[Tour]=PBlinde
    Banques[Tour+1]-=GBlinde
    Mises[Tour+1]=GBlinde
  Pot+=PBlinde+GBlinde
  # Blindes
    
  for i in Joueurs.keys():
      Joueurs[i][0] = Cartes.pop(randint(0,len(Cartes)-1)) # Joueur 1 Carte 1
      Joueurs[i][1] = Cartes.pop(randint(0,len(Cartes)-1)) # Joueur 2 Carte 2
      print(i,Joueurs[i][0],Joueurs[i][1])
  
  suivi=False
  
  templist=list(Joueurs.keys())
  for i in range(len(Listemains)):
    Listemains[i].append(Joueurs[templist[i]][0])
    Listemains[i].append(Joueurs[templist[i]][1])

  suivi=suivre(0,Tour,nbjs)
  suiviok=False
  while not suiviok:  
      fold()
      if suivi[0]=="R":
        suivi=suivre2(suivi[2],suivi[1]-1,nbjs)
      else:
        suiviok=True
    
  #Flop
  F1 = Cartes.pop(randint(0,len(Cartes)-1))
  F2 = Cartes.pop(randint(0,len(Cartes)-1))
  F3 = Cartes.pop(randint(0,len(Cartes)-1))
  flop.append(F1)
  flop.append(F2)
  flop.append(F3)
  templist=list(Joueurs.keys())
  for i in range(len(Listemains)):
        Listemains[i].append(F1)
        Listemains[i].append(F2)
        Listemains[i].append(F3)
  
  for i in range(nbjs):
      Mises[JoueursSuivent[i]]=0
  if nbjs>1:
      suiviok=False
  suivi=suivre(0,Tour,nbjs)
  while not suiviok:  
      fold()
      if suivi[0]=="R":
        suivi=suivre2(suivi[2],suivi[1]-1,nbjs)
      else:
        suiviok=True
  
  #River 
  if nbjs>1:
      suiviok=False
  F4 = Cartes.pop(randint(0,len(Cartes)-1))
  flop.append(F4)
  for i in range(len(Listemains)):
      Listemains[i].append(F4)
  for i in range(nbjs):
      Mises[JoueursSuivent[i]]=0
  suivi=suivre(0,Tour,nbjs)
  print(suiviok) #débug
  while not suiviok:  
      fold()
      if suivi[0]=="R":
        suivi=suivre2(suivi[2],suivi[1]-1,nbjs)
      else:
        suiviok=True
  
  #Turn
  if nbjs>1:
    suiviok=False
  F5 = Cartes.pop(randint(0,len(Cartes)-1))
  flop.append(F5)
  for i in range(len(Listemains)):
      Listemains[i].append(F5)
  for i in range(nbjs):
      Mises[JoueursSuivent[i]]=0
  suivi=suivre(0,Tour,nbjs)
  while not suiviok:  
      fold()
      if suivi[0]=="R":
        suivi=suivre2(suivi[2],suivi[1]-1,nbjs)
      else:
        suiviok=True
  print(F1,F2,F3,F4,F5)
  print('\n\n')
  
  for i in range(len(JoueursSuivent)):
    if Checkmain[JoueursSuivent[i]][2][0]=='QF':
      Listemains[JoueursSuivent[i]]=Checkmain[JoueursSuivent[i]][2]
      Points[JoueursSuivent[i]]=8
    elif Checkmain[JoueursSuivent[i]][0][0]=='Carre' or Checkmain[JoueursSuivent[i]][0][0]=='Full':
      Listemains[JoueursSuivent[i]]=Checkmain[JoueursSuivent[i]][0]
      if Checkmain[JoueursSuivent[i]][0][0]=='Carre':
        Points[JoueursSuivent[i]]=7
      else:
        Points[JoueursSuivent[i]]=6
    elif Checkmain[JoueursSuivent[i]][2][0]=='F':
      Listemains[JoueursSuivent[i]]=Checkmain[JoueursSuivent[i]][2]
      Points[JoueursSuivent[i]]=5
    elif Checkmain[JoueursSuivent[i]][1][0]=='Q':
      Listemains[JoueursSuivent[i]]=Checkmain[JoueursSuivent[i]][1]
      Points[JoueursSuivent[i]]=4
    else:
      Listemains[JoueursSuivent[i]]=Checkmain[JoueursSuivent[i]][0]
      if Checkmain[JoueursSuivent[i]][0][0]=='Brelan':
        Points[JoueursSuivent[i]]=3
      elif Checkmain[JoueursSuivent[i]][0][0]=='DPaire':
        Points[JoueursSuivent[i]]=2
      elif Checkmain[JoueursSuivent[i]][0][0]=='Paire':
        Points[JoueursSuivent[i]]=1
    print(Listemains[JoueursSuivent[i]])

  indl=[]
  m=Points[0]
  for i in range(len(JoueursSuivent)):
    if Points[JoueursSuivent[i]]>m:
      m=Points[JoueursSuivent[i]]
      indl=[JoueursSuivent[i]]
    elif Points[JoueursSuivent[i]]==m:
      indl.append(JoueursSuivent[i])
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
    if Listemains[win][0]=="H":
      print("Le joueur",win+1,"gagne avec un",card)
    elif Listemains[win][0]=='Brelan':
      print("Le joueur",win+1,"gagne avec un brelan de",card)
    elif Listemains[win][0]=="Full":
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
    Banques[win]=Banques[win]+Pot
  else:
    Pot=Pot//len(win)
    egal="Egalité entre les joueurs "
    for i in win:
      egal = egal + str(i+1)
      if i != win[-1]:
        egal = egal + " et "
      Banques[i]+=Pot
    print(egal)
    
  i=0
  while i<len(Listejoueurs):
    if Banques[Listejoueurs] <= 0:
      nbjv-=1
      Listejoueurs.pop(i)
    else:
      i+=1
      
  Tour+=1
  if Tour == nbjv:
    Tour = 0
  for k in range(nbjv):
    print("J",k+1,"=",Banques[k])
  print()
  print(PBlinde)
  print()
  print(Tour)

  SBanques=0
  for i in range (nbj):
    SBanques+=Banques[i]
    
  print("Débug : Argent en jeu :",SBanques)
  print("Débug : JoueursSuivent :",JoueursSuivent)
  print("Débug : Mises :",Mises)
from random import *
import random

Cartes = ['As de Pique', '2 de Pique','3 de Pique','4 de Pique','5 de Pique','6 de Pique', '7 de Pique','8 de Pique','9 de Pique','10 de Pique','Valet de Pique','Dame de Pique','Roi de Pique','As de Trefle', '2 de Trefle','3 de Trefle','4 de Trefle','5 de Trefle','6 de Trefle', '7 de Trefle','8 de Trefle','9 de Trefle','10 de Trefle','Valet de Trefle','Dame de Trefle','Roi de Trefle','As de Carreau', '2 de Carreau','3 de Carreau','4 de Carreau','5 de Carreau','6 de Carreau', '7 de Carreau','8 de Carreau','9 de Carreau','10 de Carreau','Valet de Carreau','Dame de Carreau','Roi de Carreau','As de Coeur', '2 de Coeur','3 de Coeur','4 de Coeur','5 de Coeur','6 de Coeur', '7 de Coeur','8 de Coeur','9 de Coeur','10 de Coeur','Valet de Coeur','Dame de Coeur','Roi de Coeur']
J11 = randint(0,51) # 
print(Cartes[J11])  #
Cartes.pop(J11)     #

J12 = randint(0,50)
print(Cartes[J12])
Cartes.pop(J12)

print(J11)
print(J12)

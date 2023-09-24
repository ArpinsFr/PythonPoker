from random import *
import random

Cartes = ['Ah','2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'Jh', 'Qh', 'Kh', 'Ac','2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'Jc', 'Qc', 'Kc', 'Ad','2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'Jd', 'Qd', 'Kd', 'As','2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'Js', 'Qs', 'Ks',]
J11 = randint(0,51) # Joueur 1
print(Cartes[J11])  # Carte 1
Cartes.pop(J11)     #

J12 = randint(0,50) # Joueur 1
print(Cartes[J12])  # Carte 2
Cartes.pop(J12)     #

print(J11)          # Vérifications
print(J12)

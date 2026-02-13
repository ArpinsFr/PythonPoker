import fonctions

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur





class Joueur:
    def __init__(self, nom, id, banque):
        self.nom = nom
        self.banque = banque
        self.id = id
        self.main = []
        self.mise = 0

    def quinte(self):
        main2=fonctions.numero(self.main)
        main2.sort()
        main2.reverse()
        main3=[]

        for i in main2:
            if i not in main3 :
                main3.append(i)

        if len(main3)<=4:
            return([0])
        else:
            for i in range (len(main3)-4):
                if main3[i+1]==main3[i]-1 and main3[i+2]==main3[i]-2 and main3[i+3]==main3[i]-3 and main3[i+4]==main3[i]-4:
                    return(['Q',main3[i]])
            if main3[0]==14:
                if main3[len(main3)-1]==2 and main3[len(main3)-2]==3 and main3[len(main3)-3]==4 and main3[len(main3)-4]==5:
                    return(['Q',5])
                elif main3[1]==13 and main3[2]==12 and main3[3]==11 and main3[4]==10:
                    return(['Q',14])
            return([0])



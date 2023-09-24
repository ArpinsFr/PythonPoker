def numero(main):
    main2=[]                            #  Ajoute dans la liste main2 les numeros de chaque carte
    for i in main :                     #  avec A=1 J=11 Q=12 K=13 en tant qu'entiers et pas en chaînes
        if i[0]=='T':                   #  de caractères.
            main2.append(10)            #
        elif i[0]=='A':                 #  (Plus facile pour comparer les nombres)
            main2.append(14)            #  
        elif i[0]=='J':                 #
            main2.append(11)            #
        elif i[0]=='Q':                 #
            main2.append(12)            #
        elif i[0]=='K':                 #
            main2.append(13)            #
        else :                          #
            main2.append(int(i[0]))     # -----------------------------------------------------------------
    return(main2)


def flush(main):
    H=0
    D=0
    S=0
    C=0
    for i in main :
        if i[1]=='h':
            H+=1
        if i[1]=='d':
            D+=1
        if i[1]=='s':
            S+=1
        if i[1]=='c':
            C+=1
    if H>=5 or D>=5 or S>=5 or C>=5:
        return True
    return False

def quinte(main):
    l_ind=[]
    main2=numero(main)
    for i in range(7):
        v1=main2[i]
        l_ind.append(i)
        for j in range(7):
            if main2[j]==v1+1:
                l_ind.append(j)
                v1+=1
                for i in range(7):
                    if main2[j]==v1+1:
                        l_ind.append(j)
                        v1+=1
                        for i in range(7):
                            if main2[j]==v1+1:
                                l_ind.append(j)
                                v1+=1
                                for i in range(7):
                                    if v1==13:
                                        if main2[j]==1:
                                            l_ind.append(j)
                                            for i in l_ind:
                                                l_val.append(main[i])
                                                flush=flush(l_val)
                                                if flush:
                                                    return("Quinte Flush")
                                                else : 
                                                    return("Quinte")
                                    elif main2[j]==v1+1:
                                        l_ind.append(j)
                                        for i in l_ind:
                                            l_val.append(main[i])
                                            flush=flush(l_val)
                                            if flush:
                                                return("Quinte Flush")
                                            else : 
                                                return("Quinte")
                                        else:
                                            l_ind=[]
                            else:
                                l_ind=[]
                    else:
                        l_ind=[]
            else:
                l_ind=[]
    return False




def check(main):
    main=numero(main)
    main.sort()
    main.reverse()
    Carré = False
    Brelan = False
    Full = False
    Paire = 0
    Valeur2 = 0
    CarteH = 0
    CarteH2 = 0
    CarteH3 = 0
    CarteH4 = 0
    for i in range (4):
        if main[i]==main[i+3]:
            Carré = True
            Valeur = main[i]
            if i == 0:
                CarteH = main[i+4]
            else:
                CarteH = main[0]
        else:
            for i in range (len(main)-2):
                if main[i]==main[i+2] and Brelan!=True:
                    Brelan = True
                    Valeur = main[i]
                    for i in range (len(main)-1):
                        if main[i]==main[i+1] and main[i]!=Valeur:
                            Full = True
                            Valeur2=main[i]
                    if Full == False:
                        if i==0:
                            CarteH=main[3]
                            CarteH2=main[4]
                        elif i==1:
                            CarteH=main[0]
                            CarteH2=main[4]
                        else:
                            CarteH=main[0]
                            CarteH2=main[1]
                else: 
                    for i in range (len(main)-1):
                        if Paire==0 and main[i]==main[i+1]:
                            Paire = Paire+1
                            Valeur = main[i]
                            if i==0:
                                CarteH = main[2]
                                CarteH2 = main[3]
                                CarteH3 = main[4]
                            elif i==1:
                                CarteH = main[0]
                                CarteH2 = main[3]
                                CarteH3 = main[4]
                            elif i==2:
                                CarteH = main[0]
                                CarteH2 = main[1]
                                CarteH3 = main[4]
                            else:
                                CarteH = main[0]
                                CarteH2 = main[1]
                                CarteH3 = main[2]    
                        elif Paire==1 and main[i]==main[i+1] and main[i]!=Valeur:
                            Paire = Paire+1
                            Valeur2 = main[i]
                            CarteH2 = 0
                            CarteH3 = 0
                            if Valeur!=main[0]:
                                CarteH = main[0]
                            elif Valeur2!=main[2]:
                                CarteH = main[2]
                            else:
                                CarteH = main[4]
                    if Paire==0:
                        Valeur = main[0]
                        CarteH = main[1]
                        CarteH2 = main[2]
                        CarteH3 = main[3]
                        CarteH4 = main[4]
    if Valeur == 13:
        Carte1 = "Roi"
    elif Valeur == 12:
        Carte1 = "Dame"
    elif Valeur == 11:
        Carte1 = "Valet"
    elif Valeur == 1:
        Carte1 = "As"
    else:
        Carte1 = Valeur
    if Valeur2 == 13:
        Carte2 = "Roi"
    elif Valeur2 == 12:
        Carte2 = "Dame"
    elif Valeur2 == 11:
        Carte2 == "Valet"
    elif Valeur2 == 1:
        Carte2 = "As"
    else:
        Carte2 = Valeur2
    if Carré == True:
        print( "Carré de",Carte1)
        print(CarteH)
    elif Full == True:
        print("Full aux",Carte1,"par les",Carte2)
    elif Brelan == True:
        print("Brelan de",Carte1)
        print(CarteH,CarteH2)
    elif Paire==2:
        print("Double paire de",Carte1,"et",Carte2)
        print(CarteH)
    elif Paire==1:
        print("Paire de",Carte1)
        print(CarteH,CarteH2,CarteH3)
    else:
        print("Carte haute :",Carte1)
        print(CarteH,CarteH2,CarteH3,CarteH4)

    return(main)

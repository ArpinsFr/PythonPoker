def numero(main):
    main2=[]                            #Ajoute dans la liste main2 les numeros de chaque carte
    for i in main :                     #avec A=1 J=11 Q=12 K=13 en tant qu'entiers et pas en chaînes
        if i[0]=='T':                   #de caractères.
            main2.append(10)            #(Plus facile pour comparer les nombres)
        elif i[0]=='A':
            main2.append(14) 
        elif i[0]=='J':
            main2.append(11)
        elif i[0]=='Q':
            main2.append(12)
        elif i[0]=='K':
            main2.append(13)
        else :
            main2.append(int(i[0]))
    return(main2)

def maximum(main):
    main=numero(main)
    main.reverse()
    maxi=main[0]
    return(maxi)


def flush(main):                        #Vérifie l'existence d'une flush + Quinte flush si existe
    H=0
    lh=[]
    D=0
    ld=[]
    S=0
    ls=[]
    C=0
    lc=[]
    for i in main :
        if i[1]=='h':
            H+=1
            lh.append(i)
        if i[1]=='d':
            D+=1
            ld.append(i)
        if i[1]=='s':
            S+=1
            ls.append(i)
        if i[1]=='c':
            C+=1
            lc.append(i)
    if H>4:
        if quinte(lh)==True:
            lh=numero(lh)
            if maximum(lh)==14:
                if 13 in lh and 12 in lh and 11 in lh:
                    return(["QF",14])
                else:
                    return(["QF",5])
            return(["QF",maximum(lh)])
        else:
            lh=numero(lh)
            lh.sort()
            lh.reverse()
            return(["F",lh])
    elif D>4:
        if quinte(ld)==True:
            ld=numero(ld)
            if maximum(ld)==14:
                if 13 in lh and 12 in lh and 11 in lh:
                    return(["QF",14])
                else:
                    return(["QF",5])
            return(["QF",maximum(ld)])
        else:
            ld=numero(ld)
            ld.sort()
            ld.reverse()
            return(["F",ld])
    elif S>4:
        if quinte(ls)==True:
            ls=numero(ls)
            if maximum(ls)==14:
                if 13 in lh and 12 in lh and 11 in lh:
                    return(["QF",14])
                else:
                    return(["QF",5])
            return(["QF",maximum(ls)])
        else:
            ls=numero(ls)
            ls.sort()
            ls.reverse()
            return(["F",ls])
    elif C>4:
        if quinte(lc)==True:
            lc=numero(lc)
            if maximum(lc)==14:
                if 13 in lh and 12 in lh and 11 in lh:
                    return(["QF",14])
                else:
                    return(["QF",5])
            return(["QF",maximum(lc)])
        else:
            lc=numero(lc)
            lc.sort()
            lc.reverse()
            return(["F",lc])
    return([])




def quinte(main):                       #Vérifie l'existence d'une quinte
    main2=numero(main)
    main2.sort()
    main3=[]
    dbl1=0
    dbl2=0
    for i in main2:
        if i in main3 :
            if dbl1!=0:
                dbl2=i
            else:
                dbl1=i
        else :
            main3.append(i)
    if len(main3)<=4:
        return(0)
    else:
        if main3[len(main3)-1]==14:
            if main3[0]==2 and main3[1]==3 and main3[2]==4 and main3[3]==5:
                return(5)
            elif main3[len(main3)-2]==13 and main3[len(main3)-3]==12 and main3[len(main3)-4]==11 and main3[len(main3)-5]==10:
                return(14)
        else:
            for i in range (len(main3)-4):
                if main3[i+1]==main3[i]+1 and main3[i+2]==main3[i]+2 and main3[i+3]==main3[i]+3 and main3[i+4]==main3[i]+4:
                    return(main3[i]+4)
        return(0)


def check(main):                            #Fait en gros tout le reste 
    main=numero(main)
    main.sort()
    main.reverse()
    Carre = False
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
            Carre = True
            Valeur = main[i]
            if i == 0:
                CarteH = main[4]
            else:
                CarteH = main[0]
        if Carre==True :
            return(["Carre",Valeur,CarteH])
        else:
            for i in range (len(main)-2):
                if main[i]==main[i+2] and Brelan!=True:
                    Brelan = True
                    Valeur = main[i]
                    for j in range (len(main)-1):
                        if main[j]==main[j+1] and main[j]!=Valeur:
                            Full = True
                            Valeur2=main[j]
                    if i==0:
                        CarteH=main[3]
                        CarteH2=main[4]
                    elif i==1:
                        CarteH=main[0]
                        CarteH2=main[4]
                    else:
                        CarteH=main[0]
                        CarteH2=main[1]
                    if Full==True:
                        return(["Full",Valeur,Valeur2])
                    elif Brelan==True:
                        return(["Brelan",Valeur,CarteH,CarteH2])
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
                        return(["H",Valeur,CarteH,CarteH2,CarteH3,CarteH4])                  
                    if Paire==2:
                        return(["DPaire",Valeur,Valeur2,CarteH])
                    elif Paire==1:
                        return(["Paire",Valeur,CarteH,CarteH2,CarteH3])


'''
def score(main):
    check(main.Listemains[i])
    if Paire==1:
        main.Scores.append(2)
        main.Valeurs.append(Valeur)
        main.CartesH.append(10000*CarteH+100*CarteH2+1*CarteH3)
    elif Paire==0:
        main.Scores.append(1)
        main.Valeurs.append(Valeur)
        main.CartesH.append(100000*CarteH+1000*CarteH2+10*CarteH3+CarteH4)          
'''
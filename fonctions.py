def quinte(main):
    main2=[]                            #  Ajoute dans la liste main2 les numeros de chaque carte
    for i in main :                     #  avec A=1 J=11 Q=12 K=13 en tant qu'entiers et pas en chaînes
        if i[0]=='T':                   #  de caractères.
            main2.append(10)            #
        elif i[0]=='A':                 #  (Plus facile pour comparer les nombres)
            main2.append(1)             #  
        elif i[0]=='J':                 #
            main2.append(11)            #
        elif i[0]=='Q':                 #
            main2.append(12)            #
        elif i[0]=='K':                 #
            main2.append(13)            #
        else :                          #
            main2.append(int(i[0]))     # -----------------------------------------------------------------
    return(main2)





def check(main):
    main2=[]                            #  Ajoute dans la liste main2 les numeros de chaque carte
    for i in main :                     #  avec A=1 J=11 Q=12 K=13 en tant qu'entiers et pas en chaînes
        if i[0]=='T':                   #  de caractères.
            main2.append(10)            #
        elif i[0]=='A':                 #  (Plus facile pour comparer les nombres)
            main2.append(1)             #  
        elif i[0]=='J':                 #
            main2.append(11)            #
        elif i[0]=='Q':                 #
            main2.append(12)            #
        elif i[0]=='K':                 #
            main2.append(13)            #
        else :                          #
            main2.append(int(i[0]))     # -----------------------------------------------------------------



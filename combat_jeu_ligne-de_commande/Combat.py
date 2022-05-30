import random
def combat():
    print('bienvenue sur ce jeu de combat laisser moi vous presenter les differente attaque')
    print('charge: inflige entre 5 et 10 de degat et vous inflige entre1 et 3 de dégat(+2 mana)')
    print('lance:inflige entre 1 et 5 de dégat(+10 mana)')
    print('glace:inflige 3 dégat et a 1/2 de galcer l ennemi(-3 mana)')
    print('soins: rend 4 PV(+2 mana)')
    print('potion: as 1/2 de vous rendre 10 PV')
    print('aura de glace: galce l ennemie(-3 mana)')
    print('vole vie:enleve 3 PV a l ennemi et vous les donnent')
    print('magie noir:coute 100 mana peut enlever entre -10 et 30 PV')
    print('Le mana (obligatoir pour la dernière attaque) se gagne ou se perd en faisant certaine attaque')
    a2=0
    LP=random.randint(90,100)
    PV=random.randint(90,100)
    i=random.randint(90,100)
    mana=random.randint(0,10)
    mana2=5
    print('choissisez votre mode de jeu 1=PVIA 2=PVP')
    mode=int(input('mode de jeu='))
    if mode==2:
        print('attention le mode PVP presente des bug et le joueur 2 et nommé "l ennemi"')
    print('vous avez au debut tant de PV:')
    print(PV)
    print('et l ennemi a tant de PV')
    print(LP)
    while LP>0 and PV>0:
        print('Votre Mana-->'+str(mana)+'/100')
        print('choisisez une attaque 1=charge 2=lancé 3=glace 4=soin 5=potion 6=aura de glace 7=vole vie 8=magie noir(100 mana requis)')
        a=int(input('numeros de l attaque '))
        
        if a2==3:
            g=random.randint(1,2)
            if g==1:
                print('vous êtes glacé vous ne pouvez bouger')
            elif g==2:
                if a ==1:
                    doul=random.randint(5,10)
                    LP=LP-doul
                    charge=random.randint(1,3)
                    PV=PV-charge
                    mana=mana+3
                    print('la puissance de la charge vous a fait perdre tant de PV:')
                    print(charge)
                    print('il vous reste:')
                    print(PV)
                    print('PV enlever a l ennemi:')
                    print(doul)
                    print('il lui reste:')
                    print(LP)
                    print(''+str(mana)+'/100')
                    print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
                    print('-'+str(charge)+'|                       |-'+str(doul)+'')
                    print('  |0---------------------*|')
                    print('  |_______________________|')
                    
                elif a==2:
                    doul=random.randint(1,5)
                    LP=LP-doul
                    mana=mana+10
                    print('PV enlever a l ennemi:')
                    print(doul)
                    print('il lui reste:')
                    print(LP)
                    print(''+str(mana)+'/100')
                    print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
                    print('  |                       |-'+str(doul)+'')
                    print('  |0---------------------*|')
                    print('  |_______________________|')
                elif  a==3:
                    doul=3
                    LP=LP-doul
                    mana=mana-3
                    print('PV enlever a l ennemi:')
                    print(doul)
                    print('il lui reste:')
                    print(LP)
                    print(''+str(mana)+'/100')
                    print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
                    print('  |                       |-'+str(doul)+'')
                    print('  |0---------------------*|')
                    print('  |_______________________|')
                elif a==4:
                    soin=5
                    PV=PV+soins
                    mana=mana+2
                    print('votre nombre de pv est de :')
                    print(PV)
                    print(''+str(mana)+'/100')
                    print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
                    print('  |                       |-')
                    print('+'+str(soins)+'|0                     0|')
                    print('  |_______________________|')
                elif a==5:
                    n=random.randint(0,2)
                    if  n==2:
                        print(' vous vous soigner de 10')
                        PV=PV+10
                        print('il lui vous reste tant de pv')
                        print(PV)
                    elif n==0 or n==1:
                        print('votre potion c est casser')
                        print('il lui vous reste tant de pv')
                        print(PV)
                
                elif a==6:
                    a==3
                    mana=mana-3
                elif a==7:
                    doul=3
                    soins=doul
                    LP=LP-doul
                    mana=mana-1
                    print('PV enlever a l ennemie')
                    print(doul)
                    print('il lui reste:')
                    print(LP)
                    print('PV volé a l ennemie:')
                    print(soins)
                    print('il vous reste')
                    print(PV)
                    print(''+str(mana)+'/100')
                    print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
                    print('+'+str(soins)+'|                       |-'+str(doul)+'')
                    print('  |0---------------------*|')
                    print('  |_______________________|')
                
                elif a==8:
                    if mana==100 or mana>100:
                        mana=mana-100
                        mn=random.randint(-10,30)
                        LP=LP-mn
                        print('PV enlever a l ennemie')
                        print(mn)
                        print('il lui reste:')
                        print(LP)
                        print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
                        print(  '|                       |-'+str(mana)+'')
                        print('  |0---------------------*|')
                        print('  |_______________________|')
                    elif mana<100:
                        print('vous manquez de mana :-o')
        elif  a==1:
            doul=random.randint(5,10)
            LP=LP-doul
            charge=random.randint(1,3)
            PV=PV-charge
            mana=mana+3
            print('la puissance de la charge vous a fait perdre tant de PV:')
            print(charge)
            print('il vous reste:')
            print(PV)
            print('PV enlever a l ennemi:')
            print(doul)
            print('il lui reste:')
            print(LP)
            print(''+str(mana)+'/100')
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('-'+str(charge)+'|                       |-'+str(doul)+'')
            print('  |0---------------------*|')
            print('  |_______________________|')
        elif a==2:
            doul=random.randint(1,5)
            LP=LP-doul
            mana=mana+10
            print('PV enlever a l ennemi:')
            print(doul)
            print('il lui reste:')
            print(LP)
            print(''+str(mana)+'/100')
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('  |                       |-'+str(doul)+'')
            print('  |0---------------------*|')
            print('  |_______________________|')
        elif  a==3:
            doul=3
            LP=LP-doul
            mana=mana-3
            print('PV enlever a l ennemi:')
            print(doul)
            print('il lui reste:')
            print(LP)
            print(''+str(mana)+'/100')
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('  |                       |-'+str(doul)+'')
            print('  |0---------------------*|')
            print('  |_______________________|')
        elif a==4:
            soins=5
            PV=PV+soins
            mana=mana+2
            print('votre nombre de pv est de :')
            print(PV)
            print(''+str(mana)+'/100')
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('  |                       |')
            print('+'+str(soins)+'|0                     0|')
            print('  |_______________________|')
        elif a==5:
            n=random.randint(0,2)
            if  n==2:
                print(' vous vous soigner de 10')
                PV=PV+10
                print('il lui vous reste tant de pv')
                print(PV)
            elif n==0 or n==1:
                print('votre potion c est casser')
                print('il lui vous reste tant de pv')
                print(PV)
        elif a==6:
            a=3
            mana=mana-3
        elif a==7:
            doul=3
            soins=doul
            LP=LP-doul
            PV=PV+soins
            mana=mana-1
            print('PV enlever a l ennemie')
            print(doul)
            print('il lui reste:')
            print(LP)
            print('PV volé a l ennemie:')
            print(soins)
            print('il vous reste')
            print(PV)
            print(''+str(mana)+'/100')
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('+'+str(soins)+'|                       |-'+str(doul)+'')
            print('  |0---------------------*|')
            print('  |_______________________|')
        elif a==8:
            if mana==100 or mana>100:
                mana=mana-100
                mn=random.randint(-10,30)
                LP=LP-mn
                print('PV enlever a l ennemie')
                print(mn)
                print('il lui reste:')
                print(LP)
                print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
                print(  '|                       |-'+str(mn)+'')
                print('  |0---------------------*|')
                print('  |_______________________|')
            elif mana<100:
                print('vous manquez de mana :-o')
            
        print('au tour de l ennemi')
        if mode==2:
            prin('choisisez une attaque 1=charge 2=lancé 3=glace 4=soin 5=potion 6=aura de glace 7=vole vie')
        elif mode==1:
            a2=random.randint(1,7)
        if LP<15:
            soins=8
            LP=LP+soins
            print('l ennemi c est soigner il lui reste tant de PV:')
            print(LP)
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('  |                       |')
            print('  |0                     0|''+'+str(soins)+'')
            print('  |_______________________|')
        if mana2==100 or mana2>100:
            mana2=mana2-100
            mn2=random.randint(-10,30)
            PV=PV-mn2
            print('PV enlever par l ennemie')
            print(mn2)
            print('il vous reste:')
            print(PV)
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print( '-'+str(mn2)+'|                       |')
            print('  |*---------------------0|')
            print('  |_______________________|')
        elif a==3 :
            g=random.randint(1,2)
            if g==1 or g==1:
                print('l ennemie est glacé il ne peut bouger')
            elif g==2 :
                doul2=random.randint(1,5)
                PV=PV-doul2
                mana2=mana2+10
                print('vous avez perdu tant de PV:')
                print(doul2)
                print('il vous reste:')
                print(PV)
                print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
                print('-'+str(doul2)+'|                       |')
                print('  |*---------------------0|')
                print('  |_______________________|')
        elif a2==1:
            doul2=random.randint(5,10)
            PV=PV-doul2
            charge=random.randint(1,3)
            LP=LP-charge
            print('la puissance de la charge lui a fait perdre tant de PV:')
            print(charge)
            print('il lui reste:')
            print(LP)
            print('vous avez perdu tant de PV:')
            print(doul2)
            print('il vous reste:')
            print(PV)
            mana2=mana2+3
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('-'+str(doul2)+'|                       |-'+str(charge)+'')
            print('  |*---------------------0|')
            print('  |_______________________|')
            
        elif a2==2:
            doul2=random.randint(1,5)
            PV=PV-doul2
            print('vous avez perdu tant de PV:')
            print(doul2)
            print('il vous reste:')
            print(PV)
            mana2=mana2+10
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('-'+str(doul2)+'|                       |')
            print('  |*---------------------0|')
            print('  |_______________________|')
        elif a2==3:
            doul2=3
            PV=PV-doul2
            mana2=mana2-3
            print('vous avez perdu tant de PV:')
            print(doul2)
            print('il vous reste:')
            print(PV)
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('-'+str(doul2)+'|                       |')
            print('  |*---------------------0|')
            print('  |_______________________|')
        elif a2==4:
            soins=5
            LP=LP+soins
            mana2=mana2+2
            print('l ennemi c est soigner il lui reste tant de PV:')
            print(LP)
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('  |                       |')
            print('  |0                     0|''+'+str(soins)+'')
            print('  |_______________________|')
        elif a2==5:
            n=random.randint(0,2)
            if  n==2:
                print('il se soigner de 10')
                LP=LP+10
                print('il lui reste tant de pv')
                print(LP)
            elif n==0 or n==1:
                print(' ça potion c est casser')
        
        elif a2==6:
            a2=3
            mana2=mana2-3
        elif a2==7:
            doul2=3
            soins2=doul2
            PV=PV-doul2
            LP=LP+soins2
            mana2=mana-1
            print('PV enlever par l ennemie')
            print(doul2)
            print('il vous reste:')
            print(PV)
            print('PV volé par l ennemie:')
            print(soins2)
            print('il lui reste')
            print(LP)
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('-'+str(doul2)+'|                       |+'+str(soins2)+'')
            print('  |0---------------------*|')
            print('  |_______________________|')
        
        elif LP<15:
            soins=5
            LP=LP+soins
            print('l ennemi c est soigner il lui reste tant de PV:')
            print(LP)
            print('  ____PV:'+str(PV)+'__PV ennemi:'+str(LP)+'_')
            print('  |                       |')
            print('  |0                     0|''+'+str(soins)+'')
            print('  |_______________________|')
        i=i+1
    print('nombre de tours joué:')
    print(i)
    print('si vous avez moins de 1 pv vous avez perdu mais si c est votre ennemie qui a moins de 1 pv vous avez gagner')
    print('Merci d avoir joué :-).Jeu créé et édité par Martin Fischer')
    print('Version 3.0')
combat()
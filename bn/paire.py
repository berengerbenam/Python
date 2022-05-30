# coding: utf-8
def listEven(L):
    # initialisation de la liste des nombres qui se terminent par un chiffre pair
    lEvent = []
    for n in L:
        # déterminer le dernier chiffre du nombre n
        last = n%10
        # tester si le dernier chiffre est pair
        if last % 2 == 0:
            lEvent.append(n)
    return lEvent
 
# Exemple
L = [7 , 4 , 9 , 12 , 13 , 19]
print(listEven(L)) # affiche [14, 346, 728]

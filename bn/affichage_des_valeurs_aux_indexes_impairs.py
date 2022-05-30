#coding: utf-8
def oddSum(L):
    n = len(L)
    # initialisation de la somme des éléments d'index impair
    s = 0
    for i in range(0,n):
        if i%2 != 0:
            s = s + L[i]
    return s
# Exemple
L = [3 , 2 , 5 , 11 , 21 , 4 , 7]
print(oddSum(L)) # affiche 17

# coding: utf-8
# initialisation de la liste des nombres à saisir
listNombres = []
for i in range(0,5):
    n  = int(input("Tapez la valeur d'un entier : "))
    # ajouter le nombre n à la liste
    listNombres.append(n)
# Afficher la liste des nombres saisis:
print("Voici la liste des nombres saisis : " , listNombres)

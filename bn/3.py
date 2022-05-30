# coding: utf-8
# fonction qui teste si un mot contient un chiffre ou non
def digit_in_word(word):
    # initialisation d'un compteur
    counter = 0
    for x in word:
        if x.isdigit():
            counter = counter + 1
            
    if counter > 0:
        return True
    else:
        return False
        
# fonction qui transforme une chaine en une liste en décalant les mots contenant des chiffres à la fin
def moveDigit(T):
    # transformation de la chaine texte T en une liste
    L = T.split()
    
    # initialisation de la liste des mots qui ne contiennent aucun chiffre
    L_without_digit = []
    
    # initialisation de la liste des mots qui contiennent au moins un chiffre
    L_with_digit = []  
    
    # parcourir les éléments de la liste L et rechercher les mots qui contiennent des chiffres
    for word in L:
        if digit_in_word(word):
            L_with_digit.append(word)
        else:
            L_without_digit.append(word)
            
    result = L_without_digit + L_with_digit 
            
    return result

# Exemple
T = "Python_1 created in 1991. Currently it is in version Python_3.9" 
print(moveDigit(T))
# la sorite est: 
#['created', 'in', 'Currently', 'it', 'is', 'in', 'version', 'Python_1', '1991.', 'Python_3.9']

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
 
# coding: utf-8
# fonction qui teste si un mot contient un chiffre ou non
def digit_in_word(word):
    # initialisation d'un compteur
    counter = 0
    for x in word:
        if x.isdigit():
            counter = counter + 1
            
    if counter > 0:
        return True
    else:
        return False
        
# fonction qui transforme une chaine en une liste en décalant les mots contenant des chiffres à la fin
def moveDigit(T):
    # transformation de la chaine texte T en une liste
    L = T.split()
    
    # initialisation de la liste des mots qui ne contiennent aucun chiffre
    L_without_digit = []
    
    # initialisation de la liste des mots qui contiennent au moins un chiffre
    L_with_digit = []  
    
    # parcourir les éléments de la liste L et rechercher les mots qui contiennent des chiffres
    for word in L:
        if digit_in_word(word):
            L_with_digit.append(word)
        else:
            L_without_digit.append(word)
            
    result = L_without_digit + L_with_digit 
            
    return result
 
# Exemple
T = "Python_1 created in 1991. Currently it is in version Python_3.9" 
print(moveDigit(T))
# la sorite est: 
#['created', 'in', 'Currently', 'it', 'is', 'in', 'version', 'Python_1', '1991.', 'Python_3.9']
 

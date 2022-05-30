
# coding: utf-8
# fonction qui teste si le premier caractère est identique au dernier
def first_end( s ):
    if s[0] == s[-1]:
        return True
    else:
        return False
    
# Fonction qui détermine la list des mots dont le premier caractère est identique au dernier
def list_first_end(s):
    # convertir la chaine s en une liste:
    L = s.split()
    # initialisation de la liste recherchée
    l_first_end = []
    
    for word in L:
        if first_end(word):
            l_first_end.append(word)
    return l_first_end

# Exemple
s = "radar numéro 212"
print("La list recherchée est : " , list_first_end(s))
# La sortie est : La list recherchée est :  ['radar', '212']


nom = input("Entrez votre Nom s'il vous plaît ! :")
prenom = input("Entrez votre Prenom s'il vous plaît ! :")
nationalité = input("Entrez votre Nationalité s'il vous plaît ! :")
pays = input("votre pays d'origine ! :")
age = input("Entrez votre age s'il vous plaît ! :")
#convert 
nom = str(nom)
prenom = str(prenom)
nationalité = str(nationalité)
pays = str(pays)
age = int(age)
#afficher
print("Vous appelez :  {}! {} et nationalité :{},pays : {} et votre age : {} ans".format(nom,prenom,nationalité,pays,age))

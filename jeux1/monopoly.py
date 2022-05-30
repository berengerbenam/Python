import time
import random
carte_com = ["Frais de scolarité : payez 50€",
             "Votre assurance vie vous rapporte 100€",
             "commission d'expert immobilier. Recevez 25€",
             "Les impôts vous rembourse 20€",
             "Erreur de la banque en votre faveur. Recevez 200€",
             "Vous héritez de 100€",
             "Vous avez gagné le deuxième prix de beauté, recevez 10€",
             "C'est votre anniversaire, l'adversaire doit vous donner 20€",
             "Avancez jusqu'à la case départ (recevez 200€)",
             "Frais d'hospitalisation, payez 100€"]

carte_chance = ['Avancez au boulevard de la villette en passant par la case départ (et en recevant 200€)',
                "Vous avez été élu Président du Conseil d'Administration, versez 50€ à l'adversaire.",
                "Rendez-vous à l'avenue Henri-Martin.",
                "Amende pour excès de vitesse : payez 15€ au parc gratuit",
                "Votre immeuble et votre prêt vous rapporte !! Vous devez toucher 150€.",
                "La banque vous verse un dividende de 50€",
                "Avancez à la case départ (recevez 200€).",
                "Avancez vers la compagnie de distribution des eaux",
                "Allez à la Gare de Lyon en passant par la case départ (et en recevant 200€)",
                "Relancez le dé"]
_tour_ = None
espace = ' ' * 30
joueurs = [1, 2]
posJ1 = ['case départ', 0]
propJ1 = []
argentJ1 = 1500
posJ2 = ['case départ', 0]
propJ2 = []
argentJ2 = 1500
argent_parc = 0
result = random.randint(1, 12)
t_prisonJ1 = 0
t_prisonJ2 = 0
def compteJ1():
    print("Votre compte : %s€" % argentJ1)
def compteJ2():
    print("Votre compte : %s€" % argentJ2)
def intro():
    print()
    print("%s BIENVENU DANS UN MONOPOLY PYTHON !!!!" % espace)
    print()
    time.sleep(1.5)
    print("Ce jeu ne peut malheureusement pas être un jeu à plus de deux...")
    print()
    time.sleep(2.75)
    pret = input("Quand vous serez prêt à lancer la partie, appuyez sur A : ")
    if pret == 'a' or pret == 'A':
        print()
    else:
        while pret != 'a' or pret != 'A':
            m_cmd()
            pret = input("Quand vous serez prêt à lancer la partie, appuyez sur A : ")
            if pret == 'a' or pret == 'A':
                print()
def paiement():
    print()
    time.sleep(0.75)
    print("...")
    time.sleep(0.75)
    print()
    print("Paiement en cours")
    print()
    time.sleep(0.75)
    print("...")
    time.sleep(1.5)
    print()
    print("Paiement effectué !!!")
def m_cmd():
    print()
    print("Mauvaise commande !! ")
    print()
def d():
    print()
    print("...")
    time.sleep(0.75)
    print()
    print("Lancement des dés")
    print()
    time.sleep(0.75)
    print("...")
def payJ1(nb):
    global argentJ1
    argentJ1 = argentJ1 + nb
def payJ2(nb):
    global argentJ2
    argentJ2 = argentJ2 + nb
def unpayJ1(nb):
    global argentJ1
    argentJ1 = argentJ1 - nb
def unpayJ2(nb):
    global argentJ2
    argentJ2 = argentJ2 - nb

class cases():
    def départ_début():
        for x in range(1, 3):
            print("Le joueur %s est sur la case départ" % x)
            time.sleep(0.75)
            print("Le joueur %s a 1500€" % x)
            print()
            time.sleep(1.5)
    def depart():
        print()
        time.sleep(1.5)
        print("Vous arrivez sur la case départ")
        print()
        time.sleep(0.75)
        print("Vous recevez 200€")
        print()
        if _tour_ == 1:
            payJ1(200)
            time.sleep(1.5)
            compteJ1()
            time.sleep(1.5)
            tour.j2()
        elif _tour_ == 2:
            payJ2(200)
            time.sleep(1.5)
            compteJ2()
            time.sleep(1.5)
            tour.j1()
    def propriété(adj, nom, prix, loyer):
        global propJ1
        global propJ2
        global _tour_
        print()
        print("Vous tombez sur %s" % nom)
        if nom not in propJ1 and nom not in propJ2:
            print()
            time.sleep(1.5)
            print("%s n'appartient à personne." % adj)
            print()
            time.sleep(0.75)
            print("Prix : %s€" % prix)
            print()
            achat = input("Voulez-vous l'acheter ? (oui, non) ")
            if achat == 'oui':
                print()
                print("très bien")
                print()
                time.sleep(0.75)
                if _tour_ == 1:
                    unpayJ1(prix)
                    propJ1.append(nom)
                    time.sleep(1.5)
                    compteJ1()
                elif _tour_ == 2:
                    unpayJ2(prix)
                    propJ2.append(nom)
                    time.sleep(1.5)
                    print("Votre compte : %s€" % argentJ2)
                time.sleep(0.5)
                print()
                time.sleep(0.5)
                print("%s est désormais à vous !!!" % nom)
                print()
                time.sleep(1.5)
                print("loyer : %s€" % loyer)
                if _tour_ == 1:
                    tour.j2()
                elif _tour_ == 2:
                    tour.j1()
            else:
                print()
                print("Très bien...")
                print()
                if _tour_ == 2:
                    tour.j1()
                else:
                    _tour_ =_tour_ + 1
                    if _tour_ == 2:
                        tour.j2()
        elif nom in propJ1 and _tour_ == 1 or nom in propJ2 and _tour_ == 2:
            print()
            print("%s vous appartient déjà." % nom)
            if _tour_ == 2:
                tour.j1()
            else:
                _tour_ = _tour_ + 1
                if _tour_ == 2:
                    tour.j2()
        elif nom in propJ2 and _tour_ == 1:
            print()
            print("%s appartient à l'autre joueur." % nom)
            time.sleep(1.5)
            print("Vous devez payer %s€" % loyer)
            paiement()
            unpayJ1(loyer)
            payJ2(loyer)
            print()
            compteJ1()
            print()
            time.sleep(1)
            print("Le compte du Joueur 2 : %s€" % argentJ2)
            tour.j2()
        elif nom in propJ1 and _tour_ == 2:
            print()
            print("%s appartient à l'autre joueur." % nom)
            time.sleep(1.5)
            print("Vous devez payer %s€" % loyer)
            paiement()
            unpayJ2(loyer)
            payJ1(loyer)
            print()
            print("Votre compte : %s€" % argentJ2)
            print()
            time.sleep(1)
            print("Le compte du Joueur 1 : %s€" % argentJ1)
            tour.j1()
    def caisse_com():
        global carte_com
        global posJ1
        global posJ2
        global argentJ1
        global argentJ2
        print()
        print("Vous tombez sur une case 'caisse communauté'.")
        print()
        time.sleep(0.75)
        print("...")
        time.sleep(0.75)
        print()
        print("Tirage de la carte en cours...")
        print()
        time.sleep(0.75)
        print("...")
        time.sleep(0.75)
        print()
        c = random.choice(carte_com)
        print("Votre carte : '%s'" % c)
        if _tour_ == 1:
            if c == carte_com[0]:
                unpayJ1(50)
                print()
                time.sleep(1.5)
                compteJ1()
                tour.j2()
            elif c == carte_com[1]:
                payJ1(100)
                print()
                time.sleep(1.5)
                compteJ1()
                tour.j2()
            elif c == carte_com[2]:
                payJ1(25)
                print()
                time.sleep(1.5)
                compteJ1()
                tour.j2()
            elif c == carte_com[3]:
                payJ1(20)
                print()
                time.sleep(1.5)
                compteJ1()
                tour.j2()
            elif c == carte_com[4]:
                payJ1(200)
                print()
                time.sleep(1.5)
                compteJ1()
                tour.j2()
            elif c == carte_com[5]:
                payJ1(100)
                print()
                time.sleep(1.5)
                compteJ1()
                tour.j2()
            elif c == carte_com[6]:
                payJ1(10)
                print()
                time.sleep(1.5)
                compteJ1()
                tour.j2()
            elif c == carte_com[7]:
                payJ1(20)
                unpayJ2(20)
                print()
                time.sleep(1.5)
                compteJ1()
                print()
                time.sleep(1.5)
                print("Compte du Joueur 2 : %s€" % argentJ2)
                tour.j2()
            elif c == carte_com[8]:
                print()
                time.sleep(1.5)
                cases.depart()
            elif c == carte_com[9]:
                argentJ1 = argentJ1 - 100
                print()
                time.sleep(1.5)
                compteJ1()
                tour.j2()
        elif _tour_ == 2:
            if c == carte_com[0]:
                argentJ2 = argentJ2 - 50
                print()
                time.sleep(1.5)
                compteJ2()
                tour.j1()
            elif c == carte_com[1]:
                argentJ2 = argentJ2 + 100
                print()
                time.sleep(1.5)
                compteJ2()
                tour.j1()
            elif c == carte_com[2]:
                argentJ2 = argentJ2 + 25
                print()
                time.sleep(1.5)
                compteJ2()
                tour.j1()
            elif c == carte_com[3]:
                argentJ2 = argentJ2 + 20
                print()
                time.sleep(1.5)
                compteJ2()
                tour.j1()
            elif c == carte_com[4]:
                argentJ2 = argentJ2 + 200
                print()
                time.sleep(1.5)
                compteJ2()
                tour.j1()
            elif c == carte_com[5]:
                argentJ2 = argentJ2 + 100
                print()
                time.sleep(1.5)
                compteJ2()
                tour.j1()
            elif c == carte_com[6]:
                argentJ2 = argentJ2 + 10
                print()
                time.sleep(1.5)
                compteJ2()
                tour.j1()
            elif c == carte_com[7]:
                argentJ2 = argentJ2 + 20
                argentJ1 = argentJ1 - 20
                print()
                time.sleep(1.5)
                compteJ2()
                print()
                time.sleep(1.5)
                print("Compte du Joueur 1 : %s€" % argentJ1)
                tour.j1()
            elif c == carte_com[8]:
                print()
                time.sleep(1.5)
                cases.depart()
            elif c == carte_com[9]:
                argentJ2 = argentJ2 - 100
                print()
                time.sleep(1.5)
                compteJ2()
                tour.j1()
    def impot_revenu():
        global argentJ1
        global argentJ2
        print()
        print("Vous tombez sur la case 'impôts sur le revenu'")
        print()
        time.sleep(0.75)
        print("Vous devez payer 200€")
        if _tour_ == 1:
            argentJ1 = argentJ1 - 200
            print()
            time.sleep(1.5)
            compteJ1()
            tour.j2()
        elif _tour_ == 2:
            argentJ2 = argentJ2 - 200
            print()
            time.sleep(1.5)
            compteJ2()
            tour.j1()
    def chance():
        global carte_chance
        global posJ1
        global posJ2
        global argentJ1
        global argentJ2
        global argent_parc
        print()
        print("Vous tombez sur une case 'chance'.")
        print()
        time.sleep(0.75)
        print("...")
        time.sleep(0.75)
        print()
        print("Tirage de la carte en cours...")
        print()
        time.sleep(0.75)
        print("...")
        time.sleep(0.75)
        print()
        c = random.choice(carte_chance)
        print("Votre carte : '%s'" % c)
        if c == carte_chance[0]:
           print()
           time.sleep(3)
           print()
           if _tour_ == 1:
               argentJ1 = argentJ1 + 200
               posJ1[0] = 'boulevard de la Villette'
               posJ1[1] = 11
               compteJ1()
               cases.propriété("Il", "le boulevard de la Villette", 140, 10)
           elif _tour_ == 1:
               argentJ2 = argentJ2 + 200
               posJ2[0] = 'boulevard de la Villette'
               posJ2[1] = 11
               compteJ2()
               cases.propriété("Il", "le boulevard de la Villette", 140, 10)
        elif c == carte_chance[1]:
           print()
           time.sleep(3)
           print()
           if _tour_ == 1:
               argentJ1 = argentJ1 - 50
               argentJ2 = argentJ2 + 50
               compteJ1()
               print()
               time.sleep(1.5)
               print("Joueur 2, votre Compte : %s€" % argentJ2)
               time.sleep(1.5)
               tour.j2()
           elif _tour_ == 2:
               payJ1(50)
               unpayJ2(50)
               compteJ2()
               print()
               time.sleep(1.5)
               print("Joueur 1, votre compte : %s€" % argentJ1)
               time.sleep(1.5)
               tour.j1()
        elif c == carte_chance[2]:
            print()
            time.sleep(3)
            if _tour_ == 1:
                posJ1[0] = 'avenue Henri-Martin'
                posJ1[1] = 24
            elif _tour_ == 2:
                posJ2[0] = 'avenue Henri-Martin'
                posJ2[1] = 24
            cases.propriété("Elle", "l'avenue Henri-Martin", 240, 20)
        elif c == carte_chance[3]:
            print()
            time.sleep(3)
            print()
            argent_parc = argent_parc + 15
            if _tour_ == 1:
                unpayJ1(15)
                compteJ1()
                print("Compte du Parc gratuit : %s€" % argent_parc)
                tour.j2()
            elif _tour_ == 2:
                unpayJ2(15)
                compteJ2()
                print("Compte du Parc gratuit : %s€" % argent_parc)
                tour.j1()
        elif c == carte_chance[4]:
            print()
            time.sleep(2.5)
            print()
            if _tour_ == 1:
                payJ1(150)
                compteJ1()
                time.sleep(1)
                tour.j2()
            elif _tour_ == 2:
                payJ2(150)
                compteJ2()
                time.sleep(1)
                tour.j1()
        elif c == carte_chance[5]:
            print()
            time.sleep(2.5)
            print()
            if _tour_ == 1:
                payJ1(50)
                compteJ1()
                time.sleep(1)
                tour.j2()
            elif _tour_ == 2:
                payJ2(50)
                compteJ2()
                time.sleep(1)
                tour.j1()
        elif c == carte_chance[6]:
           time.sleep(2)
           depart()
        elif c == carte_chance[7]:
           print()
           time.sleep(2)
           if _tour_ == 1:
               posJ1[0] = 'Compagnie de distribution des eaux'
               posJ1[1] = 28
           elif _tour_ == 2:
               posJ2[0] = 'Compagnie de distribution des eaux'
               posJ2[1] = 28
           cases.distrib_eaux()
        elif c == carte_chance[8]:
           print()
           time.sleep(3)
           print()
           if _tour_ == 1:
               argentJ1 = argentJ1 + 200
               posJ1[0] = 'Gare de Lyon'
               posJ1[1] = 15
               compteJ1()
           elif _tour_ == 1:
               argentJ2 = argentJ2 + 200
               posJ2[0] = 'Gare de Lyon'
               posJ2[1] = 15
               compteJ2()
           cases.propriété("Elle", "la gare de Lyon", 200, 25)
        elif c == carte_chance[9]:
           time.sleep(1.5)
           if _tour_ == 1:
               fd_J1()
           elif _tour_ == 2:
               fd_J2()
    def simple_visite():
        print()
        print("Vous tombez sur la case 'simple visite', à côté de la prison.")
        print()
        time.sleep(2.75)
        print("Rien ne se passe pour vous ce tour")
        if _tour_ == 1:
            tour.j2()
        elif _tour_ == 2:
            tour.j1()
    def prison():
        global t_prisonJ1
        global t_prisonJ2
        print()
        time.sleep(1)
        print("Vous êtes désormais sur en prison.")
        time.sleep(2)
        print("Vous devrez sauter 2 tour avant de pouvoir rejouer, à ce moment là, vous devrez payer 50€")
        if _tour_ == 1:
            t_prisonJ1 = 1
            tour.j2()
        elif _tour_ == 2:
            t_prisonJ2 = 1
            tour.j1()
    def disrib_elec():
        global propJ1
        global propJ2
        global _tour_
        print()
        print("Vous tombez sur la 'compagnie de distribution d'électricité'.")
        if 'compagnie de distribution des eaux' not in propJ1 and 'compagnie de distribution des eaux' not in propJ2:
            print()
            time.sleep(1.5)
            print("La compagnie de distribution d'électricté n'appartient à personne.")
            print()
            time.sleep(0.75)
            print("Prix : 150€")
            print()
            achat = input("Voulez-vous l'acheter ? (oui, non) ")
            if achat == 'oui':
                print()
                print("très bien")
                print()
                time.sleep(0.75)
                if _tour_ == 1:
                    unpayJ1(150)
                    propJ1.append('compagnie de distribution des eaux')
                    time.sleep(1.5)
                    compteJ1()
                elif _tour_ == 2:
                    unpayJ2(150)
                    propJ2.append('compagnie de distribution des eaux')
                    time.sleep(1.5)
                    print("Votre compte : %s€" % argentJ2)
                time.sleep(0.5)
                print()
                time.sleep(0.5)
                print("La compagnie de distribution d'électricté est désormais à vous !!!")
                print()
                time.sleep(1.5)
                print("loyer : -avec 1 seule compagnie : 4 fois le montant des dés")
                print("        -avec les 2 compagnie : 10 fois le montant des dés")
                time.sleep(3)
                if _tour_ == 1:
                    tour.j2()
                elif _tour_ == 2:
                    tour.j1()
            else:
                print()
                print("Très bien...")
                print()
                if _tour_ == 2:
                    tour.j1()
                else:
                    _tour_ =_tour_ + 1
                    if _tour_ == 2:
                        tour.j2()
        elif 'compagnie de distribution des eaux' in propJ1 and _tour_ == 1 or 'compagnie de distribution des eaux' in propJ2 and _tour_ == 2:
            print()
            print("%s vous appartient déjà." % nom)
            if _tour_ == 2:
                tour.j1()
            else:
                _tour_ =_tour_ + 1
                if _tour_ == 2:
                    tour.j2()
        elif 'compagnie de distribution des eaux' in propJ1 and _tour_ == 2 and 'compagnie de distribution des eaux' not in propJ1:
            print()
            time.sleep(1)
            print("La compagnie appartient au Joueur 1. Vous devez payer.")
            time.sleep(1)
            loyer = 4 * result
            print("Loyer : %s€ (4 fois le montant des dés)" % loyer)
            unpayJ2(loyer)
            print()
            time.sleep(2)
            compteJ2()
            tour.j1()
        elif 'compagnie de distribution des eaux' in propJ2 and _tour_ == 1 and 'compagnie de distribution des eaux' not in propJ2:
            print()
            time.sleep(1)
            print("La compagnie appartient au Joueur 2. Vous devez payer.")
            time.sleep(1)
            loyer = 4 * result
            print("Loyer : %s€ (4 fois le montant des dés)" % loyer)
            unpayJ1(loyer)
            print()
            time.sleep(2)
            compteJ1()
            tour.j2()
        elif 'compagnie de distribution des eaux' in propJ1 and _tour_ == 2 and 'compagnie de distribution des eaux' in propJ1:
            print()
            time.sleep(1)
            print("La compagnie appartient au Joueur 1. Vous devez payer.")
            time.sleep(1)
            loyer = 10 * result
            print("Loyer : %s€ (10 fois le montant des dés car l'adversaire à les deux compagnies)" % loyer)
            unpayJ2(loyer)
            print()
            time.sleep(2)
            compteJ2()
            tour.j1()
        elif 'compagnie de distribution des eaux' in propJ2 and _tour_ == 1 and 'compagnie de distribution des eaux' in propJ2:
            print()
            time.sleep(1)
            print("La compagnie appartient au Joueur 2. Vous devez payer.")
            time.sleep(1)
            loyer = 10 * result
            print("Loyer : %s€ (10 fois le montant des dés car l'adversaire à les deux compagnies)" % loyer)
            unpayJ1(loyer)
            print()
            time.sleep(2)
            compteJ1()
            tour.j2()
    def parc_gratuit():
        print()
        print("Vous tombez sur le parc gratuit")
        print()
        time.sleept(1)
        print("Il y a %s€ déposés dessus. Vous le récupérez" % argent_parc)
        print()
        timee.sleep(1)
        if _tour_ == 1:
            payJ1(argent_parc)
            compteJ1()
            tour.j2()
        elif _tour_ == 2:
            payJ2(argent_parc)
            compteJ2()
            tour.j1()
    def distrib_eaux():
        global propJ1
        global propJ2
        global _tour_
        print()
        print("Vous tombez sur la 'compagnie de distribution des eaux'.")
        if 'compagnie de distribution des eaux' not in propJ1 and 'compagnie de distribution des eaux' not in propJ2:
            print()
            time.sleep(1.5)
            print("La compagnie de distribution des eaux n'appartient à personne.")
            print()
            time.sleep(0.75)
            print("Prix : 150€")
            print()
            achat = input("Voulez-vous l'acheter ? (oui, non) ")
            if achat == 'oui':
                print()
                print("très bien")
                print()
                time.sleep(0.75)
                if _tour_ == 1:
                    unpayJ1(150)
                    propJ1.append('compagnie de distribution des eaux')
                    time.sleep(1.5)
                    compteJ1()
                elif _tour_ == 2:
                    unpayJ2(150)
                    propJ2.append('compagnie de distribution des eaux')
                    time.sleep(1.5)
                    print("Votre compte : %s€" % argentJ2)
                time.sleep(0.5)
                print()
                time.sleep(0.5)
                print("La compagnie de distribution des eaux est désormais à vous !!!")
                print()
                time.sleep(1.5)
                print("loyer : -avec 1 seule compagnie : 4 fois le montant des dés")
                print("        -avec les 2 compagnie : 10 fois le montant des dés")
                time.sleep(3)
                if _tour_ == 1:
                    tour.j2()
                elif _tour_ == 2:
                    tour.j1()
            else:
                print()
                print("Très bien...")
                print()
                if _tour_ == 2:
                    tour.j1()
                else:
                    _tour_ =_tour_ + 1
                    if _tour_ == 2:
                        tour.j2()
        elif 'compagnie de distribution des eaux' in propJ1 and _tour_ == 1 or 'compagnie de distribution des eaux' in propJ2 and _tour_ == 2:
            print()
            print("%s vous appartient déjà." % nom)
            if _tour_ == 2:
                tour.j1()
            else:
                _tour_ =_tour_ + 1
                if _tour_ == 2:
                    tour.j2()
        elif 'compagnie de distribution des eaux' in propJ1 and _tour_ == 2 and 'compagnie de distribution des eaux' not in propJ1:
            print()
            time.sleep(1)
            print("compagnie de distribution des eaux appartient au Joueur 1. Vous devez payer.")
            time.sleep(1)
            loyer = 4 * result
            print("Loyer : %s€ (4 fois le montant des dés)" % loyer)
            unpayJ2(loyer)
            print()
            time.sleep(2)
            compteJ2()
            tour.j1()
        elif 'compagnie de distribution des eaux' in propJ2 and _tour_ == 1 and 'compagnie de distribution des eaux' not in propJ2:
            print()
            time.sleep(1)
            print("La compagnie appartient au Joueur 2. Vous devez payer.")
            time.sleep(1)
            loyer = 4 * result
            print("Loyer : %s€ (4 fois le montant des dés)" % loyer)
            unpayJ1(loyer)
            print()
            time.sleep(2)
            compteJ1()
            tour.j2()
        elif 'compagnie de distribution des eaux' in propJ1 and _tour_ == 2 and 'compagnie de distribution des eaux' in propJ1:
            print()
            time.sleep(1)
            print("La compagnie appartient au Joueur 1. Vous devez payer.")
            time.sleep(1)
            loyer = 10 * result
            print("Loyer : %s€ (10 fois le montant des dés car l'adversaire à les deux compagnies)" % loyer)
            unpayJ2(loyer)
            print()
            time.sleep(2)
            compteJ2()
            tour.j1()
        elif 'compagnie de distribution des eaux' in propJ2 and _tour_ == 1 and 'compagnie de distribution des eaux' in propJ2:
            print()
            time.sleep(1)
            print("La compagnie appartient au Joueur 2. Vous devez payer.")
            time.sleep(1)
            loyer = 10 * result
            print("Loyer : %s€ (10 fois le montant des dés car l'adversaire à les deux compagnies)" % loyer)
            unpayJ1(loyer)
            print()
            time.sleep(2)
            compteJ1()
            tour.j2()
    def allez_prison():
        print()
        print("Vous tombez sur la case 'Allez en prison'.")
        time.sleep(0.5)
        print()
        time.sleep(0.5)
        cases.prison()
    def taxes_luxes():
        global argentJ1
        global argentJ2
        global argent_parc
        global _tour_
        print()
        print("Vous tomebez sur la case 'Taxes de luxe'")
        print()
        time.sleep(2)
        print("Vous devez mettre 100€ au parc gratuit")
        if _tour_ == 1:
            argentJ1 = argenJ1 - 100
            argent_parc = argent_parc + 100
        elif _tour_ == 2:
            argentJ2 = argentJ2 - 100
            argent_parc = argent_parc + 100
        
        
def fd_J1():
    global posJ1
    global argentJ1
    result = random.randint(2, 12)
    d()
    print("Vous avez fait %s." % result)
    print()
    time.sleep(0.75)
    print("Vous avancez de %s cases" % result)
    casec = posJ1[1]
    casec2 = casec + result
    del posJ1[1]
    posJ1.append(casec2)
    if posJ1[1] == 40:
        posJ1[0] = 'case départ'
        cases.depart()
    elif casec2 > 40:
        casec2 = casec2 - 40
        del posJ1[1]
        posJ1.append(casec2)
        print("Vous passez par la case départ. Vous recevez 200€")
        argentJ1 = argentJ1 + 200
        print()
    if posJ1[1] == 1:
        posJ1[0] = 'boulevard de Belleville'
        cases.propriété('Il', 'le Boulevard de Belleville', 60, 2)
    elif posJ1[1] == 2:
        posJ1[0] = 'caisse communauté'
        cases.caisse_com()
    elif posJ1[1] == 3:
        posJ1[0] = 'rue Lecourbe'
        cases.propriété('Elle', 'la rue Lecourbe', 60, 4)
    elif posJ1[1] == 4:
        posJ1[0] = 'Impôts sur le revenu'
        cases.impot_revenu()
    elif posJ1[1] == 5:
        posJ1[0] = 'Gare Montparnasse'
        cases.propriété('Elle', 'la gare Montparnasse', 200, 25)
    elif posJ1[1] == 6:
        posJ1[0] = 'rue Vaugirard'
        cases.propriété('Elle', 'La rue Vaugirard', 100, 4)
    elif posJ1[1] == 7:
        posJ1[0] = 'chance'
        cases.chance()
    elif posJ1[1] == 8:
        posJ1[0] = 'rue de Courcelles'
        cases.propriété('Elle', 'la rue de Courcelles', 100, 6)
    elif posJ1[1] == 9:
        posJ1[0] = 'avenue de la République'
        cases.propriété('Elle', "l'avenue de la République", 120, 8)
    elif posJ1[1] == 10:
        posJ1[0] = 'simple visite'
        cases.simple_visite()
    elif posJ1[1] == 11:
        posJ1[0] = 'boulevard de La Villette'
        cases.propriété('Il', 'le boulevard de La Villette', 140, 10)
    elif posJ1[1] == 12:
        posJ1[0] = "Distribution d'électricité"
        cases.distrib_elec()
    elif posJ1[1] == 13:
        posJ1[0] = "avenue de Neuilly"
        cases.propriété('Elle', "l'avenue de neuilly", 140, 10)
    elif posJ1[1] == 14:
        posJ1[0] = 'Rue de paradis'
        cases.propriété('Elle', 'la rue de Paradis', 160, 12)
    elif posJ1[1] == 15:
        posJ1[0] = "gare de Lyon"
        cases.propriété('Elle', 'la gare de Lyon', 200, 25)
    elif posJ1[1] == 16:
        posJ1[0] = "avenue Mozart"
        cases.propriété('Elle', "l'avenue Mozart", 180, 14)
    elif posJ1[1] == 17:
        posJ1[0] = "Caisse communauté"
        cases.caisse_com()
    elif posJ1[1] == 18:
        posJ1[0] = 'Boulevard St-Michel'
        cases.propriété('Il', "le boulevard St-Michel", 180, 14)
    elif posJ1[1] == 19:
        posJ1[0] = "Place Pigale"
        cases.propriété('Elle', "la place Pigale", 200, 16)
    elif posJ1[1] == 20:
        posJ1[0] = 'Parc gratuit'
        cases.parc_gratuit()
    elif posJ1[1] == 21:
        posJ1[0] = "Avenue Matignon"
        cases.propriété('Elle', "l'avenue Matignon", 220, 18)
    elif posJ1[1] == 22:
        posJ1[0] = 'Chance'
        cases.chance()
    elif posJ1[1] == 23:
        posJ1[0] = 'Boulevard Malesherbes'
        cases.propriété('Il', "le boulevard Malesherbes", 220, 18)
    elif posJ1[1] == 24:
        posJ1[0] = 'Avenue Henri-Martin'
        cases.propriété('Elle', "l'avenue Henri-Martin", 240, 20)
    elif posJ1[1] == 25:
        posJ1[0] = 'Gare du Nord'
        cases.propriété('Elle', 'la gare du Nord', 200, 25)
    elif posJ1[1] == 26:
        posJ1[0] = "Faubourg St-Honoré"
        cases.propriété('Il', "le faubourg St-Honoré", 260, 22)
    elif posJ1[1] == 27:
        posJ1 = "Place de la bourse"
        cases.propriété('Elle', "la place de la Bourse", 260, 22)
    elif posJ1[1] == 28:
        posJ1[0] = 'Compagnie de distribution des eaux'
        cases.distrib_eaux()
    elif posJ1[1] == 29:
        posJ1[0] = 'Rue La Fayette'
        cases.propriété('Elle', "la rue Lafayette", 280, 24)
    elif posJ1[1] == 30:
        posJ1[0] = 'Allez en Prison'
        posJ1[1] = 10
        cases.prison()
    elif posJ1[1] == 31:
        posJ1[0] = 'Avenue de Breuteil'
        cases.propriété('Elle', "l'avenue de Breuteil", 300, 26)
    elif posJ1[1] == 32:
        posJ1[0] = 'Avenue Foch'
        cases.propriété('Elle', "l'avenue Foch", 300, 26)
    elif posJ1[1] == 33:
        posJ1[0] = 'Caisse communauté'
        cases.caisse_com()
    elif posJ1[1] == 34:
        posJ1[0] = 'Boulevard des Capucines'
        cases.propriété('Il', "le boulevard des Capucines", 320, 28)
    elif posJ1[1] == 35:
        posJ1[0] = 'Gare St-Lazare'
        cases.propriété('Elle', "la gare St-Lazare", 200, 25)
    elif posJ1[1] == 36:
        posJ1[0] = 'Chance'
        cases.chance()
    elif posJ1[1] ==37:
        posJ1[0] = 'Avenue des Champs-Elysées'
        cases.propriété('Elle', "l'avenue des Champs-Elysées", 350, 35)
    elif posJ1[1] == 38:
        posJ1[0] = 'Taxes de luxes'
        cases.taxes_luxes()
    elif posJ1[1] == 39:
        posJ1[0] = 'Rue de la Paix'
        cases.propriété('Elle', "la rue de la paix", 400, 50)
def fd_J2():
    global posJ2
    result = random.randint(2, 12)
    d()
    print("Vous avez fait %s." % result)
    print()
    time.sleep(0.75)
    print("Vous avancez de %s cases" % result)
    case = posJ2[1]
    case2 = case + result
    del posJ2[1]
    posJ2.append(case2)
    if posJ2[1] == 40:
        posJ2[0] = 'case départ'
        cases.depart()
    elif case2 >= 40:
        case2 = case2 - 40
        del posJ2[1]
        posJ2.append(case2)
        print("Vous passez par la case départ. Vous recevez 200€")
        argentJ2 = argentJ2 + 200
        print()
        compteJ2()
    if posJ2[1] == 1:
        posJ2[0] = 'boulevard de Belleville'
        cases.propriété('Il', 'le Boulevard de Belleville', 60, 2)
    elif posJ2[1] == 2:
        posJ2[0] = 'caisse communauté'
        cases.caisse_com()
    elif posJ2[1] == 3:
        posJ2[0] = 'rue Lecourbe'
        cases.propriété('Elle', 'la rue Lecourbe', 60, 4)
    elif posJ2[1] == 4:
        posJ2[0] = 'Impôts sur le revenu'
        cases.impot_revenu()
    elif posJ2[1] == 5:
        posJ2[0] = 'Gare Montparnasse'
        cases.propriété('Elle', 'la gare Montparnasse', 200, 25)
    elif posJ2[1] == 6:
        posJ2[0] = 'rue Vaugirard'
        cases.propriété('Elle', 'La rue Vaugirard', 100, 4)
    elif posJ2[1] == 7:
        posJ2[0] = 'chance'
        cases.chance()
    elif posJ2[1] == 8:
        posJ2[0] = 'rue de Courcelles'
        cases.propriété('Elle', 'la rue de Courcelles', 100, 6)
    elif posJ2[1] == 9:
        posJ2[0] = 'avenue de la République'
        cases.propriété('Elle', "l'avenue de la République", 120, 8)
    elif posJ2[1] == 10:
        posJ2[0] = 'simple visite'
        cases.simple_visite()
    elif posJ2[1] == 11:
        posJ2[0] = 'boulevard de La Villette'
        cases.propriété('Il', 'le boulevard de La Villette', 140, 10)
    elif posJ2[1] == 12:
        posJ2[0] = "Distribution d'électricité"
        cases.distrib_elec()
    elif posJ2[1] == 13:
        posJ2[0] = "avenue de Neuilly"
        cases.propriété('Elle', "l'avenue de neuilly", 140, 10)
    elif posJ2[1] == 14:
        posJ2[0] = 'Rue de paradis'
        cases.propriété('Elle', 'la rue de Paradis', 160, 12)
    elif posJ2[1] == 15:
        posJ2[0] = "gare de Lyon"
        cases.propriété('Elle', 'la gare de Lyon', 200, 25)
    elif posJ2[1] == 16:
        posJ2[0] = "avenue Mozart"
        cases.propriété('Elle', "l'avenue Mozart", 180, 14)
    elif posJ2[1] == 17:
        posJ2[0] = "Caisse communauté"
        cases.caisse_com()
    elif posJ2[1] == 18:
        posJ2[0] = 'Boulevard St-Michel'
        cases.propriété('Il', "le boulevard St-Michel", 180, 14)
    elif posJ2[1] == 19:
        posJ2[0] = "Place Pigale"
        cases.propriété('Elle', "la place Pigale", 200, 16)
    elif posJ2[1] == 20:
        posJ2[0] = 'Parc gratuit'
        cases.parc_gratuit()
    elif posJ2[1] == 21:
        posJ2[0] = "Avenue Matignon"
        cases.propriété('Elle', "l'avenue Matignon", 220, 18)
    elif posJ2[1] == 22:
        posJ2[0] = 'Chance'
        cases.chance()
    elif posJ2[1] == 23:
        posJ2[0] = 'Boulevard Malesherbes'
        cases.propriété('Il', "le boulevard Malesherbes", 220, 18)
    elif posJ2[1] == 24:
        posJ2[0] = 'Avenue Henri-Martin'
        cases.propriété('Elle', "l'avenue Henri-Martin", 240, 20)
    elif posJ2[1] == 25:
        posJ2[0] = 'Gare du Nord'
        cases.propriété('Elle', 'la gare du Nord', 200, 25)
    elif posJ2[1] == 26:
        posJ2[0] = "Faubourg St-Honoré"
        cases.propriété('Il', "le faubourg St-Honoré", 260, 22)
    elif posJ2[1] == 27:
        posJ2 = "Place de la bourse"
        cases.propriété('Elle', "la place de la Bourse", 260, 22)
    elif posJ2[1] == 28:
        posJ2[0] = 'Compagnie de distribution des eaux'
        cases.distrib_eaux()
    elif posJ2[1] == 29:
        posJ2[0] = 'Rue La Fayette'
        cases.propriété('Elle', "la rue Lafayette", 280, 24)
    elif posJ2[1] == 30:
        posJ2[0] = 'Allez en Prison'
        posJ2[1] = 10
        cases.prison()
    elif posJ2[1] == 31:
        posJ2[0] = 'Avenue de Breuteil'
        cases.propriété('Elle', "l'avenue de Breuteil", 300, 26)
    elif posJ2[1] == 32:
        posJ2[0] = 'Avenue Foch'
        cases.propriété('Elle', "l'avenue Foch", 300, 26)
    elif posJ2[1] == 33:
        posJ2[0] = 'Caisse communauté'
        cases.caisse_com()
    elif posJ2[1] == 34:
        posJ2[0] = 'Boulevard des Capucines'
        cases.propriété('Il', "le boulevard des Capucines", 320, 28)
    elif posJ2[1] == 35:
        posJ2[0] = 'Gare St-Lazare'
        cases.propriété('Elle', "la gare St-Lazare", 200, 25)
    elif posJ2[1] == 36:
        posJ2[0] = 'Chance'
        cases.chance()
    elif posJ2[1] ==37:
        posJ2[0] = 'Avenue des Champs-Elysées'
        cases.propriété('Elle', "l'avenue des Champs-Elysées", 350, 35)
    elif posJ2[1] == 38:
        posJ2[0] = 'Taxes de luxes'
        cases.taxes_luxes()
    elif posJ2[1] == 39:
        posJ2[0] = 'Rue de la Paix'
        cases.propriété('Elle', "la rue de la paix", 400, 50)
class tour():
    def j1():
        global _tour_
        _tour_ = 1
        print()
        time.sleep(0.75)
        print()
        print()
        if t_prisonJ1 == 1:
            print("Vous êtes en prison. Vous avez passé 1 tour en prison, il ne vous en reste qu'un.")
            t_prisonJ2 = 2
            tour.j2()
        elif t_prisonJ1 == 2:
            print("Vous êtes en prison. Vous avez passé 2 tour en prison, il ne vous en reste plus aucun.")
            t_prisonJ2 = 0
            tour.j2()
        else:
            print("Joueur 1, c'est votre tour")
            time.sleep(1.5)
            print()
            print("votre position : %s" % posJ1[0])
            print("Vos propiétés : %s" % propJ1)
            compteJ1()
            time.sleep(5)
            print()
            d = input("Apuyez sur 'd' pour lancer les dés : ")
            if d == 'd':
                fd_J1()
            else:
                while d != 'd':
                    m_cmd()
                    d = input("Apuyez sur 'd' pour lancer les dés : ")
                    if d == 'd':
                        fd_J1()
    def j2():
        global _tour_
        global t_prisonJ2
        _tour_ = 2
        print()
        time.sleep(0.75)
        print()
        print()
        if t_prisonJ2 == 1:
            print("Vous êtes en prison. Vous avez passé 1 tour en prison, il ne vous en reste qu'un.")
            t_prisonJ2 = 2
            tour.j1()
        elif t_prisonJ2 == 2:
            print("Vous êtes en prison. Vous avez passé 2 tour en prison, il ne vous en reste plus aucun.")
            t_prisonJ2 = 0
            tour.j1()
        else:
            print("Joueur 2, c'est votre tour.")
            time.sleep(1.5)
            print()
            print("votre position : %s" % posJ2[0])
            print("Vos propiétés : %s" % propJ2)
            compteJ2()
            time.sleep(5)
            print()
            d = input("Apuyez sur 'd' pour lancer les dés : ")
            if d == 'd':
                fd_J2()
            else:
                while d != 'd':
                    m_cmd()
                    d = input("Apuyez sur 'd' pour lancer les dés : ")
                    if d == 'd':
                        fd_J2()
intro()
print()
cases.départ_début()
tour.j1()

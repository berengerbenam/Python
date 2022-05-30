# -*- coding: utf-8 -*-


# Importations:
import pygame
from pygame.locals import *
import os
import pickle
import random
import sys


# Déclaration des couleurs:
GREY = (179, 177, 145)
ORANGE = (237, 127, 16)
ROUGE = (255, 0, 0)
VERT = (52, 201, 36)


# Définitions des fonctions:
def event_loop():
    """ Fonction supportant la boucle évenementielle."""
    global again, in_action, in_action_bis, nu_head_position, program

    for event in pygame.event.get():
        if event.type == QUIT:
            program = False
            again = False

        elif event.type == KEYDOWN:
            # NB: Le serpent ne pourra pas se retourner sur lui-même:
            if event.key == K_UP and in_action != "K_DOWN":
                in_action = "K_UP"
                in_action_bis = True
                nu_head_position[1] -= 20

            elif event.key == K_DOWN and in_action != "K_UP":
                in_action = "K_DOWN"
                in_action_bis = True
                nu_head_position[1] += 20

            elif event.key == K_RIGHT and in_action != "K_LEFT":
                in_action = "K_RIGHT"
                in_action_bis = True
                nu_head_position[0] += 20

            elif event.key == K_LEFT and in_action != "K_RIGHT":
                in_action = "K_LEFT"
                in_action_bis = True
                nu_head_position[0] -= 20

    # Si le joueur n'a rien saisi, le serpent bougera dans la même direction:
    if in_action_bis == False:
        if in_action == "K_UP":
            nu_head_position[1] -= 20
        elif in_action == "K_DOWN":
            nu_head_position[1] += 20
        elif in_action == "K_RIGHT":
            nu_head_position[0] += 20
        elif in_action == "K_LEFT": 
            nu_head_position[0] -= 20
    
    # On remet la variable globale in_action_bis valant False:
    in_action_bis = False


def update():
    """Fonction mettant à jour les données contenu
    de l'évènement passé."""
    global food_position, old_food_position, score, snake_positions

    # Quand le serpent se déplace "normalement":
    if nu_head_position != food_position:
        # Suppression de la queue du serpent:
        snake_positions.pop(-1)

        # Insertion d'une nouvelle tête:
        snake_positions.insert(0, list(nu_head_position))

    # Quand le serpent mange la nourriture:
    elif nu_head_position == food_position:
        # Insertion d'une nouvelle tête à l'emplacement de la nourriture:
        snake_positions.insert(0, food_position)
        # Incrémentation du score:
        score += 7
        # On enregistre l'emplacement de l'ancienne nourriture (pour la fonction draw()):
        old_food_position = food_position
        # On génère un nouvel emplacament au "hasard" pour la nourriture:
        while True:
            food_position = [random.randrange(0, 500, 20), random.randrange(100, 500, 20)]
            if food_position not in snake_positions:
                break

    # Si le serpent sort de la surface de jeu ou si il se mord la queue:
    if snake_positions[0][0] < 0 or snake_positions[0][0] > 480 or snake_positions[0][1] < 100 or snake_positions[0][1] > 480 or snake_positions[0] in snake_positions[1:]:
        # On appelle la fonction game_over()
        game_over()


def draw():
    """Fonction dessin (mise en mémoire tampon)."""
    global food, score_surface, snake_positions

    # On efface l'écran:
    screen.fill((0, 0, 0))
    # On dessine une zone zone de score:
    pygame.draw.rect(screen, (VERT), Rect(0, 0, 500, 100), 1)
    # On crée une nouvelle surface pour le score lui-même:
    score_surface = california_font.render("SCORE: "+str(score), True, (ORANGE))
    # On colle la surface du score lui-même:
    screen.blit(score_surface, (0, 0))
    # On colle la surface du meilleur score:
    screen.blit(best_score_surface, (0, 30))
    # On colle la surface de l'image cartoon du serpent dans la zone de score pour la décorer:
    screen.blit(cartoon_snake, (240, 10))

    # Si le serpent mange:
    if nu_head_position == old_food_position:
        # On colle la surface MIAM!:
        screen.blit(miam_surface, (280, 0))

        # On dessine une surface de jeu:
        pygame.draw.rect(screen, (VERT), Rect(0, 100, 500, 400), 1)

        # On dessine les éléments du serpent:
        for index, item in enumerate(snake_positions):
            # On dessine la tête en orange:
            if index == 0:
                pygame.draw.rect(screen, (ORANGE), Rect(item[0], item[1], 20, 20))
            # On dessine le reste du corps en vert:
            else:
                pygame.draw.rect(screen, (VERT), Rect(item[0], item[1], 20, 20))

    else:
        # On dessine une surface de jeu:
        pygame.draw.rect(screen, (VERT), Rect(0, 100, 500, 400), 1)

        # On dessine les éléments du serpent:
        for index, item in enumerate(snake_positions):
            # On dessine la tête en orange (contours uniquement):
            if index == 0:
                pygame.draw.rect(screen, (ORANGE), Rect(item[0], item[1], 20, 20), 2)
            # On dessine le reste du corps en vert (contours uniquement):
            else:
                pygame.draw.rect(screen, (VERT), Rect(item[0], item[1], 20, 20), 2)

    # On dessine la nourriture:
    food = pygame.draw.rect(screen, (GREY), Rect(food_position[0], food_position[1], 20, 20), 2)


def game_over():
    """Fonction de game_over, dessin (mise en mémoire tampon), affichage."""
    global again, in_action, nu_head_position, program

    # Enregistrement éventuel du score:
    # Si une score a été récupéré (fichier best_score.txt existant) alors on le compare au score effectué (Si ce dernier est > on enregistre):
    try:
        if score > best_score_recupere:
            with open("./best_score.txt", "wb") as fichier:
                mon_pickler = pickle.Pickler(fichier)
                mon_pickler.dump(score)
    # Si aucun score n'a été récupéré (fichier best_score.txt inexistant) alors on enregistre le score effectué:
    except NameError:
        with open("./best_score.txt", "wb") as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(score)

    # Collage de la surface du game over:
    screen.blit(game_over_surface, game_over_surface_rect)
    # Collage de la surface rejouer:
    screen.blit(rejouer_surface, rejouer_surface_rect)
    # Affichage général
    pygame.display.flip()

    # On maintient l'affichage tant que l'utilisateur n'a pas pris la décision de quitter ou de rejouer:
    user_choice = False
    while not user_choice:
        for event in pygame.event.get():
            if event.type == QUIT:
                user_choice = True
                program = False
                again = False
                #  J'ajoute sys.exit(0) sinon un dernier déplacement du snake sera affiché avant la fermeture du programme.
                sys.exit(0)

            # Si le joueur clique gauche souris sur rejouer:
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and (180 <= event.pos[0] <= 300) and (280 <= event.pos[1] <= 305):
                user_choice = True
                program = False


def main_loop():
    while program:
        # Gestion des évènements:
        event_loop()
        # Mise à jour:
        update()
        # Dessin (mise en mémoire tampon):
        draw()
        # Affichage:
        pygame.display.flip()
        # Cadencage à 10 FPS:
        timer.tick(10)


again = True
while again:
    # INITIALISATION DE PYGAME  #
    pygame.init()               #
    #############################


    # FENETRE #####################################
    # Création d'une fenêtre:                     #
    screen = pygame.display.set_mode((500, 500))  #
    # Modification du nom de la fenêtre:          #
    pygame.display.set_caption("rodeoshellsnake") #
    ###############################################


    # SCORE ZONE  ##############################################################################################
    # Dessin de la zone de score:                                                                              #
    score_zone = pygame.draw.rect(screen, (VERT), Rect(0, 0, 500, 100), 1)                                     #
                                                                                                               #
    # Création d'une variable score initialisée à zéro:                                                        #
    score = 0                                                                                                  #
    # Chargement d'une font:                                                                                   #
    california_font = pygame.font.Font("./California.ttf", 32)                                                 #
    # Création d'une surface pour le score lui-même:                                                           #
    score_surface = california_font.render("SCORE: "+ str(score), True, (ORANGE))                              #
    # Collage de la surface du score lui-même:                                                                 #
    screen.blit(score_surface, (0, 0))                                                                         #
                                                                                                               #
    # Création d'une surface pour l'image cartoon du serpent:                                                  #
    cartoon_snake = pygame.image.load("./cartoon_snake.png").convert_alpha()                                   #
    # Collage de la surface de l'image cartoon du serpent dans la zone de score pour la décorer:               #
    screen.blit(cartoon_snake, (240, 10))                                                                      #
                                                                                                               #
    # Création d'une surface miam:                                                                             #
    miam_surface = california_font.render("MIAM!", True, (ORANGE))                                             #
                                                                                                               #
    # Si un fichier des meilleurs scores existe, création d'une surface et affichage (sinon, on affiche 0):    #
    if os.path.exists("best_score.txt"):                                                                       #
        with open("./best_score.txt", "rb") as fichier:                                                        #
            mon_depickler = pickle.Unpickler(fichier)                                                          #
            best_score_recupere =  mon_depickler.load()                                                        #
        best_score_surface = california_font.render("Best: " + str(best_score_recupere), True, (ORANGE))       #
    else:                                                                                                      #
        best_score_surface = california_font.render("Best : 0", True, (ORANGE))                                #
    screen.blit(best_score_surface, (0, 30))                                                                   #
    ############################################################################################################


    # SNAKE_FOOD_ZONE  #############################################################################################
    # Dessin de la zone de jeu:                                                                                    #
    snake_food_zone = pygame.draw.rect(screen, (VERT), Rect(0, 100, 500, 400), 1)                                  #
                                                                                                                   #
    # Dessin du serpent et mise en variable de sa position:                                                        #
    snake = pygame.draw.rect(screen, (ORANGE), Rect(0, 240, 20, 20), 2)                                            #
    snake_positions = [[0, 240]]                                                                                   #
                                                                                                                   #
    # Dessin de la nourriture et mise en variable de sa position:                                                  #
    food = pygame.draw.rect(screen, (GREY), Rect(240, 240, 20, 20), 2)                                             #
    food_position = [240, 240]                                                                                     #
                                                                                                                   #
    # Création d'une surface pour le game over:                                                                    #
    game_over_surface = california_font.render("G A M E    O V E R!", True, (ROUGE))                               #
    # Création d'un rectangle pour la surface game over (dans un but futur (lors de l'affichage) de centrage):     #
    game_over_surface_rect = game_over_surface.get_rect(midtop=(240, 240))                                         #
                                                                                                                   #
                                                                                                                   #
    # Création d'une surface pour rejouer:                                                                         #
    rejouer_surface = california_font.render("PLAY AGAIN", True, (ORANGE))                                         #
    # Création d'un rectangle pour la surface rejouer (dans un but futur (lors de l'affichage) de centrage):       #
    rejouer_surface_rect = rejouer_surface.get_rect(midtop=(240, 280))                                             #
    ################################################################################################################


    # FPS & TIMER  ##############
    # Nombre de FPS:            #
    fps = 10                    #
    # Création d'un objet clock:#
    timer = pygame.time.Clock() #
    #############################


    # AFFICHAGE GENERAL  ###
    pygame.display.flip()  #
    ########################

    # VARIABLES GLOBALES servant au déplacement du serpent #
    in_action = "K_RIGHT"                                  #
    in_action_bis = bool()                                 #
    ########################################################

    # VARIABLE GLOBALE servant au déplacement du serpent  #
    nu_head_position = [0, 240]                           #
    #######################################################

    # VARIABLE GLOBALE utile à l'affichage de la surface MIAM!  #
    old_food_position = []                                      #
    #############################################################

    # VARIABLE GLOBALE servant à la boucle contenue dans la fonction main_loop()  #
    program = True                                                                #
    #############Coded#by#rodeoshell###############################################

    main_loop()

pygame.quit()
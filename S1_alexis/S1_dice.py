#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 22:37:08 2019

@author: alexis
"""
import numpy as np
import random
from random import randint
 
##########################################
##          S1 Exo 8
########################################## 
## fonction permetant de simuler le tir du dé
## une liste simule les valeurs du dé auqu'elle nous tirons au sort dedans avec random
def tirage_de():
    de = [1,2,3,4,5,6]
    return random.choice(de)

## à chaque tour du joueur nous tirons le dé jusqu'a obtenir la valeur de 1 pour sortir de sont tour
## chaque point es stocker dans une liste. Nous vérifions que la liste ne dépasse pas le score de 100 (fin du jeux)
def tour_joueur(liste):
    if not(isinstance(liste, list)):
        raise ValueError( ' il faut passer une liste')
    valeur_de=tirage_de()
    if(valeur_de==1 or sum(liste)>100):
        return liste
    else:
        liste.append(valeur_de)
## fonction permetant à chaque tour de joueur de noté une pause et d'afficher les résultat
## j'ai du désactiver la fonction raw_input permetant la saissi pour que les tests fonctionne
def com_utilisateur(pc,joueur1):
    print('C\'est maintenant votre tour')
    print('votre score es : ' ,  sum(joueur1))
    print('le score de votre adversaire : ' , sum(pc))
    #raw_input("Entrez le code  ")


## fonction apellant les autre fonction pour nous permettre à l'utilisateur de jouer 
def shuffle(joueur1):
    if not(isinstance(joueur1, list)):
        raise ValueError( ' il faut passer une liste')
    pc=[] 
    tour=1
    while (sum(joueur1)<100) and (sum(pc)<100) :
        if tour==1:
            com_utilisateur(pc,joueur1)
            tour_joueur(joueur1)
            tour=0
        elif tour==0:
            tour_joueur(pc)
            tour=1
    return joueur1,pc           
    


## nous décrivons à l'utilisateur le début du jeux et le score finale après le jeux
print("Bienvenue dans ce jeux de dé")

joueur1=[] 
resultat_joueur,resultat_pc=shuffle(joueur1)
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print('fin du jeu')
print('score joueur :  ', sum(resultat_joueur))
print('score pc : ', sum(resultat_pc))
          

if(sum(joueur1)>sum(resultat_pc)):
    print('vous avez gagner')
else: 
    print(' vous avez perdu')

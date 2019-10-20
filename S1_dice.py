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

def tirage_de():
    de = [1,2,3,4,5,6]
    return random.choice(de)
    
 
def shuffle(joueur1):
    if not(isinstance(joueur1, list)):
        raise ValueError( ' il faut passer une liste')
    pc=[]
    tour=0
    while (sum(joueur1)<100) and (sum(pc)<100) :
        tirage=tirage_de()
        if tirage==1:
            if tour==1:
                tour=0
            else:
                tour=1
        else:
            if tour==1:
               joueur1.append(tirage) 
            if tour==0:
                pc.append(tirage)
                
    if(sum(joueur1)>sum(pc)):
        gagnant="vous avez gagner"
    else: 
        gagnant="vous avez perdu" 
    return joueur1,gagnant


 
print("Bienvenue dans ce jeux de dé")
joueur1=[]            
resultat_joueur,gagnant=shuffle(joueur1)
print(gagnant)
print("votre socre es ")
print(sum(resultat_joueur))
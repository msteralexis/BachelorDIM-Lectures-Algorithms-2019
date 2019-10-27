
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:17:13 2019

@author: escudera
"""

import numpy as np
import random as rand

print (' Programme Session 1 / Alexis Escudero !!')

##########################################
##          Exo 1
##########################################

 ## réponse au question 
## question 1 : 
    ## cela nous métra rien 
## question 2: 
    ## si divisions par zéro ou nombre négatif alors sa plante 

## Dans cette fonction on souhaite effectuer la somme d'un tableau en paramètre par valeur 
## on aura un tableau deux variables sont créées (une pour la somme des nombres du tableau l'autre pour le nombre total des nombres contenu dans le tableau) 
## une condition vient vérifier si les nombres sont strictement bien positif
## Je test si on envoie bien un tableau à la fonction sinon on retourn un message d'erreur 
def average_above_zero(table):
    if not(isinstance(table, list)):
        raise ValueError( ' il faut passer une liste')   
    som = 0
    n = 0
    for i in range(len(table)):
        if table[i] > 0:
            som = som+table[i]
            n=n+1
    if n==0:
        return 0
    else: 
        return som/n
    
##########################################
##          Exo 2
##########################################


## Dans cette fonction on passe par valeur un tableau
## on control si on n'as bien passer un tableau 
## On parcour le tableau on stock la valeur la plus grande ainsi que sont indice dans deux variable intermédiaire 
def max_value(table):
    if not(isinstance(table, list)):
        raise ValueError( ' il faut passer une liste') 
    valeur_max=table[0]
    indice=0
    for i in range(len(table) ):
        if (table[i]> valeur_max):
            valeur_max=table[i]
            indice=i
    return(valeur_max,indice)



##########################################
##          Exo 3
##########################################
## Dans cztte fonction souhaite inverser un tableau passer en paramère par valeur
## Ici on utilise une fonction déjà existante reverse()
## on retourne ensuite le ableau modifier 
def reverse_table_bis(table):
    if not(isinstance(table, list)):
        raise ValueError( ' il faut passer une liste') 
    table.reverse()
    return table
    
## Dans cztte fonction souhaite inverser un tableau passer en paramère par valeur
## Ici on utilise une boucle while pour parcourire nore tableau 
## deux compeur un pointant sur le premier élément et le deuxième le dernier élément du tableau
## On inverse les valeurs grace au deux compteur et une variable stockan une des valeur en attendant
## Une condiions permet de sortir de la boucle pour les tableau au nompbre de case impaire 
## on retourne ensuite le ableau modifier 
def reverse_table(table):
    if not(isinstance(table, list)):
        raise ValueError( ' il faut passer une liste') 
    nb_element=(int((len(table)) /2)) -1
    i=0
    compt=len(table)-1
    while i <= nb_element:
        stock=table[i]
        table[i]=table[compt]
        table[compt]=stock    
        compt=compt-1
        i=i+1
    return table


##########################################
##          Exo 4
##########################################
def roi_bbox(img): 
    point_bas=0
    point_droit=0
    point_gauche=img.shape[1]
    point_haut=0
    for idrow in range (img.shape[0]):
        for idcol in range (img.shape[1]):
            pixval=[idrow,idcol] 
            ''' on étermie du point bas '''
            if  img[idrow,idcol]>=1:
                if point_bas < idrow :
                    point_bas=idrow
                    coordoner_bas=pixval
                if point_haut==0:
                    coordoner_haut=pixval
                    point_haut=1
                if point_droit < idcol:
                    point_droit=idcol
                    coordoner_droit=pixval
                if point_gauche > idcol:
                    coordoner_gauche=pixval
                    point_gauche=idcol
      
    if point_bas!=0 and point_haut!=0 and point_droit!=0 :        
        tab_coordoner=np.eye(4,2)
        ##coordoner point 1 du rectangle 
        tab_coordoner[0,0]=coordoner_haut[0]
        tab_coordoner[0,1]=coordoner_gauche[1]
        ##coordoner point 2 du rectangle 
        tab_coordoner[1,0]=coordoner_haut[0]
        tab_coordoner[1,1]=coordoner_droit[1]
        ##coordoner point 3 du rectangle 
        tab_coordoner[2,0]=coordoner_bas[0]
        tab_coordoner[2,1]=coordoner_droit[1]
        ##coordoner point 4 du rectangle 
        tab_coordoner[3,0]=coordoner_bas[0]
        tab_coordoner[3,1]=coordoner_gauche[1]
        return  tab_coordoner
    else:
        return 0






##########################################
##          Exo 5
##########################################
## Dans cette exercice il nous passons à notre fonction 2 paramètre 
## une matrice 2D de types caractère vide et un entier.
## Nous souhaitons remplir x case du tableau en fonction de la valeur de notre entier
## Pour commencer la fonction control si Nous passons bien un entier nomé ici K 
## et si le nombre de case du tableau es suffisant pa rapport à la valeur de k
## Pour générer une case au assard dans notre matrice 2 liste mélanger prendront la
## valeur de x et de y.
## nous controlons à chaue fois si la case es bien vide grace à une fonction définie 
## si la case es vide alors nous lui donnons comme nouvelle valeur un chiffre donner par la fonction alea()
## nous renvoyont le tableau avec les case remplit
import random
from random import randint


def alea():
    return rand.randint(0,6)


def case_vide(char):
    if(char==''):
        return 1
    else:
        return 0


def random_fill_sparse(table_parametre, k):
    if not(isinstance(k, int)):
        raise ValueError( ' il faut passer un entier') 
    table=table_parametre
    tailletab= np.shape(table)
    nc_case_tab=tailletab[0]+tailletab[1]
    if (nc_case_tab<k):
        raise ValueError( 'tableau trops petit par rapprt au nombre d element que vous souhaitez integrer') 
   

    liste_x=range(0,tailletab[0])
    liste_y=range(0,tailletab[1])
    i=0
    while (i < k ):
        x=random.choice(liste_x) 
        y=random.choice(liste_y) 
        if (case_vide(table[x,y])==1):
            
            table[x,y]=alea()
            i=i+1
    return table


##########################################
##          Exo 6
##########################################
## Dans cette exercice nous souhaitons envoyer une chaine de caractère en paramètre pour suprimer les espaces
## nous controlons dans un premier temps si c'est bien uen chaine qui nous es renvoyer 
## si c'est le cas nous utiliser la fonction Replace de l'objet pour suprimer les espaces.
## chaine_amodifier qui sont définie de la manière suivant ' '  nosu retournons le resultat
def remove_whitespace(chaine_amodifier):
    if not(isinstance(chaine_amodifier, str)):
        raise ValueError( ' il faut passer une chaine de caractere ') 
    table_renverser=chaine_amodifier.replace(' ','')
    return table_renverser


##########################################
##          Exo 7
##########################################


## Dans cette exercice nous souhaitons passer en paramètre une liste
## une liste avec le même contenut devra être renvoyer mais melanger au hassard
    
## Dans cette premier fonction nous utiliserons la fonction melanger une liste exstante dans numpy
def shuffle_bis(liste):
    if not(isinstance(liste, list)):
        raise ValueError( ' il faut passer une liste') 
    random.shuffle(liste)
    return liste
    

## Dans cette autre fonction nous devons dans une premier temps déterminer la taille de notre liste
## 2 liste sont initialiser, la première contiendrat les indice tirer au sort a l'aide de la fonction Randint
## la seconde contiendrat les valeurs piocher au hasard dans la liste passer en paramèttre
## une condition permet de vérifier que le numero tirer avec randint n'es pas déj& contenu dans la liste d'indice
def shuffle(liste):
    if not(isinstance(liste, list)):
        raise ValueError( ' il faut passer une liste') 
    taille_liste=len(liste)
    liste_indice=[]
    liste_melanger=[]
    i=0
    while (i < taille_liste ):
        a=randint(0, (taille_liste-1))
        if  not (a in  liste_indice ):
            liste_indice.append(a)
            liste_melanger.append(liste[a])
            i=i+1
    return liste_melanger




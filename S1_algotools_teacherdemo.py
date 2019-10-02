
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:17:13 2019

@author: escudera
"""

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
def reverse_table(table):
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
def reverse_table2(table):
    if not(isinstance(table, list)):
        raise ValueError( ' il faut passer une liste') 
    nb_element_able_div_2=(int((len(table)) /2)) -1
    i=0
    compt=len(table)-1
    while i <= nb_element_able_div_2:
        stock=table[i]
        table[i]=table[compt]
        table[compt]=stock    
        compt=compt-1
        i=i+1
    return table

##test function reverse_table2()
table=[1,2,3,4,6]
print(table)
tablezz=reverse_table2(table)
print(table)
print(tablezz)



##########################################
##          Exo 4
##########################################
''' on importe une bibliothèque pour gérer les image '''






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


import cv2
import numpy as np

''' on importe l'image '''
img2=cv2.imread('exoquatre.png',0)
alexis=roi_bbox(img2)
                
print(alexis)

matrix=np.zeros((10,10), dtype=np.int32) 
matrix[3:6, 4:8]=np.ones((3,4), dtype=np.int32)
alexis2=roi_bbox(matrix)
print(alexis2[0,0])
print(alexis2)




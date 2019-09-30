
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:17:13 2019

@author: escudera
"""

print (' Programme Session 1 / Alexis Escudero')

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
            som = som+tab[i]
            n=n+1
    if n==0:
        return 0
    else: 
        return som/n
    
##test  average_above_zero
tab=[1,2,3,4,5,6]
som=average_above_zero(tab)
if som==0:
    print('erreur que des nombre négatifs')
else: 
    print ('la somme vault ', som)



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
        if (tab[i]> valeur_max):
            valeur_max=tab[i]
            indice=i
    return(valeur_max,indice)

##test function max_value

## Test valeur max pour chiffre négatif  
tab=[-5,-8]
valeur_max,indice=max_value(tab)
print('valeur max = ',valeur_max)
print('indice valeur = ',indice)

## Test valeur max pour chiffre positif
tab=[1,2,3,4,5,6]
valeur_max,indice=max_value(tab)
print('valeur max = ',valeur_max)
print('indice valeur = ',indice)

## Test si on lui envoi bien un tableau
##tab=12
##valeur_max,indice=max_value(tab)



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
    

##test function reverse_table()
table=[1,2,3,4,5,6]
print(table)
table_inverser=reverse_table(table)
print(table_inverser)



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
print(tablezz)



##########################################
##          Exo 4
##########################################
''' on importe une bibliothèque pour gérer les image '''
#import cv2

''' on importe l'image '''
#img=cv2.imread('exo4.png',0)

''' permet d'afficher l'image dans une fenêtre  
cv2.imshow('read image',img)
cv2.waitKey()
'''



'''teste prof '''
import numpy as np

'''oncréer une matrice qu'avec des zeros'''
matrix=np.zeros((10,10), dtype=np.int32) 

''' dans ce tableau je viens lui rentrer des valeur = 1 '''
matrix[3:6, 4:8]=np.ones((3,4), dtype=np.int32)
matrix[3,8]=1
matrix[2,6]=1
matrix[6,6]=1



point_bas=0
point_droit=0
point_gauche=matrix.shape[1]
point_haut=0




for idrow in range (matrix.shape[0]):
    for idcol in range (matrix.shape[1]):
        pixval=[idrow,idcol] 
        print(pixval)
        ''' on étermie du point bas '''
        if  matrix[idrow,idcol]==1:
            
            if point_bas < idrow :
                point_bas=idrow
                coordoner_bas=[idrow,idcol]
            if point_haut==0:
                coordoner_haut=[idrow,idcol]
                point_haut=1
                
            if point_droit < idcol:
                point_droit=idcol
                coordoner_droit=[idrow,idcol]
          
            if point_gauche > idcol:
                coordoner_gauche=[idrow,idcol]
                point_gauche=idcol
                
              

       

print(coordoner_droit)
print(coordoner_bas)
print(coordoner_haut)


print(coordoner_gauche)


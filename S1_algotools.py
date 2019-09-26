# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:17:13 2019

@author: escudera
"""

print (' Programme Session 1 / Alexis Escudero')


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


''' partie teste '''

##########################################
##test  average_above_zero
tab=[1,2,3,4,5,6]
som=average_above_zero(tab)
if som==0:
    print('erreur que des nombre négatifs')
else: 
    print ('la somme vault ', som)



##########################################
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
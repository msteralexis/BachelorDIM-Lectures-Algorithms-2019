# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:17:13 2019

@author: escudera
"""

print (' Programme Session 1 / Alexis Escudero')


''' # réponse au question 
# question 1 : 
    # cela nous métra rien 
" question 2: 
    # si divisions par zéro ou nombre négatif alors sa plante 
'''


'''
# Dans cette fonction on souhaite effectuer la somme d'un tableau en paramètre par valeur 
# on aura un tableau deux variables sont créées (une pour la somme des nombres du tableau l'autre pour le nombre total des nombres contenu dans le tableau) 
# une condition vient vérifier si les nombres sont strictement bien positif
'''
def average_above_zero(table:list):
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


#test  average_above_zero
tab=[1,2,3,4,5,6]
som=average_above_zero(tab)
if som==0:
    print('erreur que des nombre négatifs')
else: 
    print ('la somme vault ', som)


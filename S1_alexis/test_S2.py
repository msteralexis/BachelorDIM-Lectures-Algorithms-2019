#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:44:54 2019

@author: alben
"""

import pytest
import numpy as np
import random
from random import randint
import S1_algotools as tobetested
import numpy as np
import S1_dice as dice

        
##########################################
##          Exo 1
##########################################
        
## on test si la somme es faite correcttement
def test_average_above_zero_1():
    tab=[1,2,3,4,5,6]
    som=tobetested.average_above_zero(tab)
    assert som == 3,5
 ## on test si la fonction prend en compte uniquement les nombre négatif
def test_average_above_zero_2():
    tab=[-1,-2,-3,-4,-5,-6]
    som=tobetested.average_above_zero(tab)
    assert som==0
    
 ## on test si la fonction renvoi une erreur si on lui passe autre chose qu'un tableau 
def test_average_above_zero_3():
    tab="vive le vent !!"
    with pytest.raises(ValueError):
        tobetested.average_above_zero(tab)
    
        
##########################################
##          Exo 2
##########################################
## on test si la fonction renvoi une erreur si on lui passe autre chose qu'un tableau 
def test_max_value_1():
    tab="vive le vent !!"
    with pytest.raises(ValueError):
        tobetested.max_value(tab)

## test si les nombre négatif fonctionne
def test_max_value_2():
    tab=[-5,-8]
    valeur_max,indice=tobetested.max_value(tab)
    assert valeur_max== -5
    assert indice== 0
## test si les nombre positif fonctionne
def test_max_value_3():
    tab=[1,2,6,4,5,9]
    valeur_max,indice=tobetested.max_value(tab)
    assert valeur_max== 9
    assert indice== 5


##########################################
##          Exo 3
##########################################
    
    ## test fonction existante 
def test_reverse_table_bis_1():
    tab="vive le vent !!"
    with pytest.raises(ValueError):
        tobetested.reverse_table_bis(tab)

## test tableau avec nombre element pair 
def test_reverse_table_bis_2():        
    tab=[1,2,3,4,5,6]
    tab_test=[6,5,4,3,2,1]
    table_inverser= tobetested.reverse_table_bis(tab)
    assert table_inverser==tab_test
    assert tab==tab_test

    
## test fonction réaliser par moi même 
def test_reverse_table_1(): 
    tab="vive le vent !!"
    with pytest.raises(ValueError):
        tobetested.reverse_table(tab)
        
## test tableau avec nombre element pair 
def test_reverse_table_2():        
    tab=[1,2,3,4,5,6]
    tab_test=[6,5,4,3,2,1]
    table_inverser=tobetested.reverse_table(tab)
    assert table_inverser== tab_test
    assert tab==tab_test
 
## test avec un tableau avec nombre élément impair
def test_reverse_table_3():        
    tab=[1,2,3,4,6]
    tab_test=[6,4,3,2,1]
    table_inverser= tobetested.reverse_table(tab)
    assert tab==tab_test
    assert table_inverser== tab_test
    
##########################################
##          Exo 4
##########################################
    
    
def test_roi_bbox_1():
    matrix=np.zeros((10,10), dtype=np.int32) 
    matrix[3:6, 4:8]=np.ones((3,4), dtype=np.int32)
    tab_coordoner=tobetested.roi_bbox(matrix)
    assert tab_coordoner[0,0]==3
    assert tab_coordoner[0,1]==4
    assert tab_coordoner[1,0]==3
    assert tab_coordoner[1,1]==7
    assert tab_coordoner[2,0]==5
    assert tab_coordoner[2,1]==7
    assert tab_coordoner[3,0]==5
    assert tab_coordoner[3,1]==4

def test_roi_bbox_2():
    matrix=np.zeros((10,10), dtype=np.int32) 
    tab_coordoner=tobetested.roi_bbox(matrix)
    assert tab_coordoner==0
    
##########################################
##          Exo 5
##########################################
## on test la fonction alea() nous renvoi bien un nombre 
def test_alea():
    nb_test=tobetested.alea()
    assert type(nb_test)== int
## On test si notre fonction evaluer si une case es vide ou non fonctionne
def test_case_vide_1():
    tab_casevide=['','a']
    res=tobetested.case_vide(tab_casevide[0])
    assert res==1
    
def test_case_vide_2():
    tab_casevide=['','a']
    res=tobetested.case_vide(tab_casevide[1])
    assert res==0
    
    
## on test si on passer k autre chose qu'un entier nous avons bien uen erreur    
def test_random_fill_sparse_2():
    table=[1,2,3,4]
    k='a' 
    with pytest.raises(ValueError):
        tobetested.random_fill_sparse(table, k)
        
## on test la remonter d'erreur si on rentre un nombre de case à remplir supèrieur au nombre de case du tableau 
def test_random_fill_sparse_3():
    table = np.chararray((4,4))
    k=10
    with pytest.raises(ValueError):
        tobetested.random_fill_sparse(table, k)

## On test si notre fonction nous remplit correctement notre tableau 
def test_random_fill_sparse_4():
    table=['0','1','2','3','4','5','6']
    table = np.chararray((4,4))
    table[:]=''
    k=2
    res=tobetested.random_fill_sparse(table, k)
    assert res.all == table.all
  
    
##########################################
##          Exo 6
##########################################
## on test la remonte d'erreur si on passe autre chose qu'une chaine de caractère 
def test_remove_whitespace_1():   
    alexis=10
    with pytest.raises(ValueError):
        tobetested.remove_whitespace(alexis)
## On test si notre fonction suprimer bien les caractère 
def test_remove_whitespace_2():   
    alexis=' aalexis effectuent un test'
    res= tobetested.remove_whitespace(alexis)   
    assert res=='aalexiseffectuentuntest'
        
    
##########################################
##          Exo 7
##########################################
    
## on viens tester ici notre fonction "déja existante" 
## on test sir notre fonction control bien l'envoi dune liste 
def test_shuffle_bis_1():
    tab="vive le vent !!"
    with pytest.raises(ValueError):
        tobetested.shuffle_bis(tab)
       
## on test sir notre fonction nou renvoit bien une liste de la même taille
def test_shuffle_bis_2():
    liste=['a','b','c','d']
    liste_melanger=tobetested.shuffle_bis(liste)
    assert len(liste)== len(liste_melanger)
    
## on vérifier que le contenu de notre liste renvoyer es bien le même que la liste originale
def test_shuffle_bis_3():
    liste=['a','b','c','d']
    liste_melanger2=tobetested.shuffle_bis(liste)
    taille_liste=len(liste)
    i=0
    while (i < taille_liste):
        assert liste[i] in liste_melanger2
        i=i+1
    
  
## on viens tester ici notre fonction "manuel"
        
## on test sir notre fonction control bien l'envoi dune liste     
def test_shuffle_4():
    tab="vive le vent !!"
    with pytest.raises(ValueError):
        tobetested.shuffle(tab)
        
## on test sir notre fonction nou renvoit bien une liste de la même taille      
def test_shuffle_5():
    liste_test2=['a','b','c','d']
    liste_melanger2=tobetested.shuffle(liste_test2)
    assert len(liste_test2)== len(liste_melanger2)
 
    
## on vérifier que le contenu de notre liste renvoyer es bien le même que la liste originale
def test_shuffle_6():
    liste=['a','b','c','d']
    liste_melanger2=tobetested.shuffle(liste)
    taille_liste=len(liste)
    i=0
    while (i < taille_liste):
        assert liste[i] in liste_melanger2
        i=i+1
        
        
     
##########################################
##          S1 Exo 8
########################################## 
def test_tirage_de():
    de = [1,2,3,4,5,6]
    retourr=dice.tirage_de()
    assert retourr in de
    
 ## on test si la fonction renvoi une erreur si on lui passe autre chose qu'une liste                    
def test_tour_joueur_parametre():
    de = "vive le vent"
    with pytest.raises(ValueError):
        dice.tour_joueur(de)
        
## on détermine si notre fonction renvoi bien un entier      
def test_tour_joueur_retour():
    liste_test=[] 
    retour=dice.tour_joueur(liste_test)
    assert 0== isinstance(retour, int)
    
   
 ## on test si la fonction renvoi une erreur si on lui passe autre chose qu'une liste  
def test_shuffle_parametre():
    de = "vive le vent"
    with pytest.raises(ValueError):
        dice.shuffle(de)
        
def test_suffle_retour():
    joueur1=[] 
    resultat_joueur,resultat_pc=dice.shuffle(joueur1)
    assert 0== isinstance(resultat_joueur, int)
    assert 0== isinstance(resultat_pc, int)
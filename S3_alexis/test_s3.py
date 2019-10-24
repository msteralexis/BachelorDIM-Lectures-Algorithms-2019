#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 22:26:40 2019

@author: alexis
"""

import pytest
import S3_imgproc_tools as S3
import numpy as np
import cv2

###########################################################################################
##              Partie 1 
###########################################################################################

## on effectuent une fonction test pour chaque fonction qui renverrat la couleurs inverser de l'image
## Dans une premier temps on doit charger l'image
## On effectue l'inversison d'une couleur sur un pixel de l'image. Sela nous servirat comme valeurs de test
def test_invert_colors_manual():
    image_couleur=np.array([ np.random.randint(255, size=(3, 3)) ])
    pixel_test=255-image_couleur[0,0]
    S3.invert_colors_manual(image_couleur)
    assert pixel_test.all()==image_couleur[0,0].all()

## on teste si les paramètre passer sont controler 
def test_invert_colors_manual_parametre():
    test_parametre="on effectuent un test"
    with pytest.raises(ValueError):
        S3.invert_colors_manual(test_parametre)
## test si la fonction utilisant la bilbiothèque numpy fonctionne
def test_invert_colors_numpy():
    image_couleur=np.array([ np.random.randint(255, size=(3, 3)) ])
    pixel_test=255-image_couleur[0,0]
    S3.invert_colors_numpy(image_couleur)
    assert pixel_test.all()==image_couleur[0,0].all()

## on teste si les paramètre passer sont controler     
def test_invert_colors_numpy_parametre():
    test_parametre="on effectuent un test"
    with pytest.raises(ValueError):
        S3.invert_colors_numpy(test_parametre)
    
## test si la fonction utilisant la bilbiothèque opencv fonctionne
def test_invert_colors_opencv():
    image_couleur=np.array([ np.random.randint(255, size=(3, 3)) ])
    pixel_test=255-image_couleur[0,0]
    S3.invert_colors_opencv(image_couleur)
    assert pixel_test.all()==image_couleur[0,0].all()
## on teste si les paramètre passer sont controler 
def test_invert_colors_opencv_parametre():
    test_parametre="on effectuent un test"
    with pytest.raises(ValueError):
        S3.invert_colors_opencv(test_parametre)
    
    
    
## long et fastidieu nous répétont beaucoups de code avec la versions précédente.
## Il serai par conséquent beaucoups plus judicieux d'effectuer un bloque fonctionelle appelant 
## toutes les fonction à la fois et nous renvoyant un entier correspondant au nombre de fonction qui on réussis
## pour ce faire nosu fessons appel à la fonction test_image du fichier S3_imgproc_tool.py  
        
def test_pixel_inverser():
    image_couleur=np.array([ np.random.randint(255, size=(3, 3)) ])
    image_inverser=S3.invert_colors_opencv(image_couleur)
    resultat=S3.test_pixel(image_couleur,image_inverser)
    assert resultat==0
    
    
## Cette fonction nous permet de teste la bonne exécutions de tous nos bloque fonctionelles
def test_all_function():
    image_couleur=np.array([ np.random.randint(255, size=(3, 3)) ])
    compteur_test=S3.test_image2(image_couleur)
    assert compteur_test==3
    
## on teste si les paramètre passer sont controler     
def test_all_function_parametre():
    test_parametre="on effectuent un test"
    with pytest.raises(ValueError):
        S3.test_image2(test_parametre)
    
    
## Nous souhaitons obtenir le temps d"éxécutions de nos fonctions d'inversions 
## de couleurs sur des images de taille differentes
  


def test_time_image_parametre():
    test_parametre="on effectuent un test"
    with pytest.raises(ValueError):
        S3.time_image(test_parametre)
       
def test_delai_execution_comparer():
    time=S3.delai_execution_comparer()
    assert 1== isinstance(time, list)

###########################################################################################
##              Partie 2
###########################################################################################

def test_threshold_image_manual():
    imagee=cv2.imread("../S3_image_test/480.jpg")
    image_nb=S3.threshold_image_manual(imagee)
    assert 255 in image_nb
    assert 0 in image_nb
    
## on teste si les paramètre passer sont controler     
def test_threshold_image_manual_parametre():
    test_parametre="on effectuent un test"
    with pytest.raises(ValueError):
        S3.threshold_image_manual(test_parametre)
        
## on teste si les paramètre passer sont controler 
def test_threshold_image_numpy_parametre():
    test_parametre="on effectuent un test"
    with pytest.raises(ValueError):
        S3.threshold_image_numpy(test_parametre)
        
def test_threshold_image_numpy():
    imagee=cv2.imread("../S3_image_test/480.jpg")
    img=S3.threshold_image_numpy(imagee)
    assert 255 in img
    assert 0 in img
    
def threshold_colors_opencv():
    n=np.arange(0,255)
    imagee=cv2.imread("../S3_image_test/480.jpg")
    image_nb=S3.threshold_colors_opencv(imagee)
    assert image_nb.all() in n.all() 
## on teste si les paramètre passer sont controler 
def threshold_colors_opencv_parametre():
    test_parametre="on effectuent un test"
    with pytest.raises(ValueError):
        S3.threshold_colors_opencv(test_parametre)


  
    
def time_image_noir_blanc_parametre():
    test_parametre="on effectuent un test"
    with pytest.raises(ValueError):
        S3.time_image_noir_blanc(test_parametre)
    
    
def test_alexis():
    test_retour=S3.delai_execution_comparer_image_noir_blanc()
    assert 1== isinstance(test_retour, list)
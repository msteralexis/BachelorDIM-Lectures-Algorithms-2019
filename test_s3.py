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



## on effectuent une fonction test pour chaque fonction qui renverrat la couleurs inverser de l'image
## Dans une premier temps on doit charger l'image
## On effectue l'inversison d'une couleur sur un pixel de l'image. Sela nous servirat comme valeurs de test
def test1():
    image_couleur=cv2.imread("exo5.jpeg")
    pixel_test=255-image_couleur[0,0]
    valeur_retour=S3.invert_colors_manual(image_couleur)
    assert pixel_test.all()==image_couleur[0,0].all()


def test2():
    image_couleur=cv2.imread("exo5.jpeg")
    pixel_test=255-image_couleur[0,0]
    valeur_retour=S3.invert_colors_numpy(image_couleur)
    assert pixel_test.all()==image_couleur[0,0].all()
    

def test3():
    image_couleur=cv2.imread("exo5.jpeg")
    pixel_test=255-image_couleur[0,0]
    valeur_retour=S3.invert_colors_opencv(image_couleur)
    assert pixel_test.all()==image_couleur[0,0].all()
    
    
## long et fastidieu nous répétont beaucoups de code avec la versions précédente.
## Il serai par conséquent beaucoups plus judicieux d'effectuer un bloque fonctionelle appelant 
## toutes les fonction à la fois et nous renvoyant un entier correspondant au nombre de fonction qui on réussis
## pour ce faire nosu fessons appel à la fonction test_image du fichier S3_imgproc_tool.py  
def test_all_function():
    image_couleur=cv2.imread("exo5.jpeg")
    compteur_test=S3.test_image2(image_couleur)
    assert compteur_test==3
    
    
## Nous souhaitons obtenir le temps d"éxécutions de nos fonctions d'inversions 
## de couleurs sur des images de taille differentes

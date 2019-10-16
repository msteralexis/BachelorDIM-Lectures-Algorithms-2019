# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:54:10 2019

@author: escudera
"""

print (' Programme Traitement Image / Alexis Escudero !!')

import cv2
import numpy as np
import time

tmps1=time.clock()
######################################################################
##                  Exercice 1 / Sans fonction prédefinie
######################################################################


## inverse les couleur d'une image colorer 
## Dans cette fonction on nous envoie un tableau 3d représentant les couleurs primaire
## rouge,bleu,vert pour un pixel. Nous devrons donc avoir 3 boucle pour parcourire tous les "coordoner"
## des coulurs d'un pixels pour l'inverser.
def invert_colors_manual(img):
    for row in range(img.shape[0]):
        for col in range (img.shape[1]):
            for cha in range(img.shape[2]):
                img[row,col,cha]=255-img[row,col,cha]
    return img




######################################################################
##                  Exercice 2  / NUMPY
######################################################################
## inverse les couleur avec la fonction près définie de Numpy
def invert_colors_numpy(img):
    img=255-img
    return img


######################################################################
##                  Exercice 3   / CV
######################################################################
## inverse les couleur avec la fonction près définie de OpenCV2

def  invert_colors_opencv(input_img):
    return cv2.bitwise_not(input_img)
   
 
    

def test_image(image,fonction):
    pixel_test=255-image[0,0]
    if(fonction ==0 ):
        image_inverse=  invert_colors_manual(image)
    if(fonction ==1 ):
        image_inverse= invert_colors_numpy(image) 
    if(fonction ==2 ):
       image_inverse= invert_colors_opencv(image)
    if (pixel_test.all()==image[0,0].all()):
        return 0
    else :
        return 1


    
def test_pixel(image,image_inverser):
    pixel_test=255-image[0,0]
    if (pixel_test.all()==image_inverser[0,0].all()):
        return 0
    else :
        return 1
    
    
  ## fonction permetant de regourper en 1 test toutes les fonctions  
def test_image2(image):
    i=0
    image_inverse= invert_colors_manual(image)
    if( test_pixel(image,image_inverse)==0):
       i=i+1
    image_inverse= invert_colors_numpy(image) 
    if( test_pixel(image,image_inverse) == 0):
       i=i+1   
    image_inverse= invert_colors_opencv(image)
    if( test_pixel(image,image_inverse) ==0):
       i=i+1
    return i
 
 
   
    

## Sur le même modèle que le bloque fonctionelle test_image2() 
## Nous réalisons une fonction nous servant pour le calcule de temps sur tous
    ## les bloque fonctionelles
 
def time_image(image):
    tmps1=time.clock()
    image_inverse= invert_colors_manual(image)
    tmps2=time.clock()
    
    tmps3=time.clock()
    image_inverse= invert_colors_numpy(image) 
    tmps4=time.clock()
    
    tmps5=time.clock()
    image_inverse= invert_colors_opencv(image)
    tmps6=time.clock()
    
    return (tmps2 - tmps1),(tmps4 - tmps3) , (tmps6 - tmps5)








cv2.waitKey()
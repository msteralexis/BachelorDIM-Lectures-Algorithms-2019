# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:54:10 2019

@author: escudera
"""

print (' Programme Traitement Image / Alexis Escudero !!')

import cv2
import numpy as np
import time

## cette variable nous permetrat de vérifier avec la fonction isinstance si le type de paramètre 
## passer dans nos fonction es bien  une image 
image_test=np.array([ np.random.randint(255, size=(3, 3)) ])

######################################################################
##                  Exercice 1 / Sans fonction prédefinie
######################################################################


## inverse les couleur d'une image colorer 
## Dans cette fonction on nous envoie un tableau 3d représentant les couleurs primaire
## rouge,bleu,vert pour un pixel. Nous devrons donc avoir 3 boucle pour parcourire tous les "coordoner"
## des coulurs d'un pixels pour l'inverser.
def invert_colors_manual(img):
    if not(isinstance(img, type(image_test))):
        raise ValueError( ' il faut passer une image') 
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
    if not(isinstance(img, type(image_test))):
        raise ValueError( ' il faut passer une image') 
    img=255-img
    return img


######################################################################
##                  Exercice 3   / CV
######################################################################
## inverse les couleur avec la fonction près définie de OpenCV2
def  invert_colors_opencv(input_img):
    if not(isinstance(input_img, type(image_test))):
        raise ValueError( ' il faut passer une image') 
    return cv2.bitwise_not(input_img)
   
 

## fonction permetant de regourper en 1 test toutes les fonctions  d'inversion de couleurs
def test_pixel(image,image_inverser):
    pixel_test=255-image[0,0]
    if (pixel_test.all()==image_inverser[0,0].all()):
        return 0
    else :
        return 1


def test_image2(image):
    if not(isinstance(image, type(image_test))):
        raise ValueError( ' il faut passer une image') 
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
    if not(isinstance(image, type(image_test))):
        raise ValueError( ' il faut passer une image') 
    resultat = []
    
    tmps1=time.clock()
    image_inverse= invert_colors_manual(image)
    tmps2=time.clock()
    resultat.append(['invert_colors_manual', tmps2 - tmps1])
 
    tmps3=time.clock()
    image_inverse= invert_colors_numpy(image) 
    tmps4=time.clock()
    resultat.append(['invert_colors_numpy', tmps4 - tmps3])
    
    tmps5=time.clock()
    image_inverse= invert_colors_opencv(image)
    tmps6=time.clock()
    resultat.append(['invert_colors_opencv', tmps6 - tmps5])
    return resultat

## On compare le temps d'éxécution de nos fonctions
def delai_execution_comparer():
    resultat_t=[]
    image_4k=cv2.imread("../S3_image_test/4k.jpeg") 
    resultat_t.append([time_image(image_4k)])
    image_720p=cv2.imread("../S3_image_test/720p.jpg")
    resultat_t.append([time_image(image_720p)])
    image_480p=cv2.imread("../S3_image_test/480.jpg")
    resultat_t.append([time_image(image_480p)])
    return resultat_t
    





##############################################################
    ## Partie  2
##############################################################
## dans cette exercice nosu souhaitons partir d'une image couleur
## (donc tableaux avec à chaque cellus 3 informations representant les couleur primaire )
## Pour passer l'image en noir et blanc tous les valeurs représentant un pixels devront donc être 
## égale à 0 ou 255 (blnc ou noir) . 
##Nous devons donc réaliser une moyenne de nos 3 couleur primaire qui à l'aide d'un seuil 
## nous indiquera si ce pixel prendra la valeur du blanc ou du noir 
def threshold_image_manual(imagee): 
    if not(isinstance(imagee, type(image_test))):
        raise ValueError( ' il faut passer une image') 
    seuil_image=55
    ## parcour des colones
    for i in range(len(imagee)):
        ## parcour des lignes
        for j in range(len(imagee[i])):
            if ((sum(imagee[i,j])/3)>seuil_image):
                imagee[i][j]=255
            else:
                imagee[i][j]=0
    return imagee 

## On utilise la fonction prédéfini de Numpy pour passer l'image en noir et blanc
def threshold_image_numpy(imagee):
    if not(isinstance(imagee, type(image_test))):
        raise ValueError( ' il faut passer une image') 
    return np.dot(imagee[...,:3], [0, 255, 0])

    
## Même principe que la fonction précédente sauf qu'il existe une fonction prédéfinie dans  open cv2  
## Les valeurs des 3 couleurs primaire prendront exactement la même entre 0 et 255 
def threshold_colors_opencv(image):
    if not(isinstance(image, type(image_test))):
        raise ValueError( ' il faut passer une image') 
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)




## on passe en paramètre une image sous forme de tableau pour l'apeller dans les trois focntion développer ci-dessus
## n calcule le temsp d'éxécutions pour toutes les fonctions
def time_image_noir_blanc(image):
    if not(isinstance(image, type(image_test))):
        raise ValueError( ' il faut passer une image') 
    resultat = []
    
    tmps1=time.clock()
    image_inverse= threshold_image_manual(image)
    tmps2=time.clock()
    resultat.append(['threshold_image_manual', tmps2 - tmps1])
 
    tmps3=time.clock()
    image_inverse= threshold_image_numpy(image) 
    tmps4=time.clock()
    resultat.append(['threshold_image_numpy', tmps4 - tmps3])
    
    tmps5=time.clock()
    image_inverse= threshold_colors_opencv(image)
    tmps6=time.clock()
    resultat.append(['threshold_colors_opencv', tmps6 - tmps5])
    return resultat

## On compare le temps d'éxécution de nos fonctions selon différentes images que l'on vas chercher dans un dossier spécifique
def delai_execution_comparer_image_noir_blanc():
    resultat_t=[]
    image_4k=cv2.imread("../S3_image_test/4k.jpeg") 
    resultat_t.append([time_image_noir_blanc(image_4k)])
    image_720p=cv2.imread("../S3_image_test/720p.jpg")
    resultat_t.append([time_image_noir_blanc(image_720p)])
    image_480p=cv2.imread("../S3_image_test/480.jpg")
    resultat_t.append([time_image_noir_blanc(image_480p)])
    return resultat_t






cv2.waitKey()
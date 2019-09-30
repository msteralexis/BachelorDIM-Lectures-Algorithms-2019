# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:54:10 2019

@author: escudera
"""

print (' Programme Traitement Image / Alexis Escudero !!')

import cv2 
import numpy as np 

#import image 
img_gray=cv2.imread("exoquatre.png",0) 
img_bgr=cv2.imread("exocinq.png",1) 
img=cv2.imread("exocinq.png") 


cv2.imshow("BGR image", img)
cv2.waitKey()
#dpermet de connaitre la tailel d'une image 
print("Gray levels image shape = "+str(img_gray.shape))
print("BGR image shape = "+str(img_bgr.shape))
## renvoi le nombre de ligne, colone et couleur




## faire un bloque fonctionelle avec ca  + TEST

##inverse une image 
for row in range(img.shape[0]):
    for col in range (img.shape[1]):
        for cha in range(img.shape[2]):
            img[row,col,cha]=255-img[row,col,cha]

## autre opération possible 
img=255-img







## permet d'afficher une image 
cv2.imshow("BGR image", img)
cv2.waitKey()



#display the loaded images
cv2.imshow("Gray levels image", img_gray)
cv2.imshow("BGR image", img_bgr)
cv2.waitKey()
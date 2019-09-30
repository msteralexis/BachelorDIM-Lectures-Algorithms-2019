#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:17:01 2019

@author: alben
"""

#############################
# Assignement 1:
# average of only the positive table values
#.... this is an ugly code
# FIXME : find out error cases
def average_above_zero(tab):
    pos_val_sum=0
    nElem=0
    for id in range(len(tab)):
        if tab[id] >0:
            nElem+=1
            pos_val_sum+=tab[id]
            lastID=id

    if nElem==0:
	raise ZeroDivisionError('No positive element found in provided list')
    return pos_val_sum/nElem, lastID           
    
#test section
tab_list=[1,2,3,-4,6,-9]
test, lastID=average_above_zero(tab_list)
print('test_sum=',test)

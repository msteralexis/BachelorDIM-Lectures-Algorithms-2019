#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:44:54 2019

@author: alben
"""

import pytest
import S1_algotools_teacherdemo as tobetested
import numpy as np

'''
def test_average_above_zero_working1():
	tab_list=[1,2,3,-4,6,-9]
	test, lastID=tobetested.average_above_zero(tab_list)
	assert test==3

def test_average_above_zero_divideZero():
	tab_list=[-1,-2,-3,-4,-6,-9]
	with pytest.raises(ZeroDivisionError):
		tobetested.average_above_zero(tab_list)
	
	

def inc(x):
    return x+1

def test_inc():
    assert inc(3)==4

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1/0
'''
        
##########################################
##          Exo 1
##########################################
        
## on test si la somme es faite correcttement
def test_exo1_1():
    tab=[1,2,3,4,5,6]
    som=tobetested.average_above_zero(tab)
    assert som == 3,5
 ## on test si la fonction prend en compte uniquement les nombre négatif
def test_exo1_2():
    tab=[-1,-2,-3,-4,-5,-6]
    som=tobetested.average_above_zero(tab)
    assert som==0
    
 ## on test si la fonction renvoi une erreur si on lui passe autre chose qu'un tableau 
def test_exo1_3():
    tab="vive le vent !!"
    with pytest.raises(ValueError):
        tobetested.average_above_zero(tab)
    
        
##########################################
##          Exo 2
##########################################
## on test si la fonction renvoi une erreur si on lui passe autre chose qu'un tableau 
def test_exo2_1():
    tab="vive le vent !!"
    with pytest.raises(ValueError):
        tobetested.max_value(tab)

## test si les nombre négatif fonctionne
def test_exo2_2():
    tab=[-5,-8]
    valeur_max,indice=tobetested.max_value(tab)
    assert valeur_max== -5
    assert indice== 0
## test si les nombre positif fonctionne
def test_exo2_3():
    tab=[1,2,3,4,5,6]
    valeur_max,indice=tobetested.max_value(tab)
    assert valeur_max== 6
    assert indice== 5


##########################################
##          Exo 3
##########################################
    
    ## test fonction existante 
def test_exo3_1():
    tab="vive le vent !!"
    with pytest.raises(ValueError):
        tobetested.reverse_table(tab)

## test tableau avec nombre element pair 
def test_exo3_2():        
    tab=[1,2,3,4,5,6]
    tab_test=[6,5,4,3,2,1]
    table_inverser= tobetested.reverse_table(tab)
    assert table_inverser==tab_test
    assert tab==tab_test

    
## test fonction réaliser par moi même 
def test_exo3_3(): 
    tab="vive le vent !!"
    with pytest.raises(ValueError):
        tobetested.reverse_table2(tab)
        
## test tableau avec nombre element pair 
def test_exo3_4():        
    tab=[1,2,3,4,5,6]
    tab_test=[6,5,4,3,2,1]
    table_inverser=tobetested.reverse_table2(tab)
    assert table_inverser== tab_test
    assert tab==tab_test
 
## test avec un tableau avec nombre élément impair
def test_exo3_5():        
    tab=[1,2,3,4,6]
    tab_test=[6,4,3,2,1]
    table_inverser= tobetested.reverse_table2(tab)
    assert tab==tab_test
    assert table_inverser== tab_test
    
##########################################
##          Exo 4
##########################################
    
    
def test_exo4_1():
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

def test_exo4_2():
    matrix=np.zeros((10,10), dtype=np.int32) 
    tab_coordoner=tobetested.roi_bbox(matrix)
    assert tab_coordoner==0
    
##########################################
##          Exo 5
##########################################
def test_exo5_1():
    tab_casevide=['','a']
    res=tobetested.case_vide(tab_casevide[0])
    assert res==1
    res=tobetested.case_vide(tab_casevide[1])
    assert res==0
    
def test_exo5_2():
    table=[1,2,3,4]
    k='a'
    with pytest.raises(ValueError):
        tobetested.random_fill_sparse(table, k)

def test_exo5_3():
    table = np.chararray((4,4))
    k=10
    with pytest.raises(ValueError):
        tobetested.random_fill_sparse(table, k)

def test_exo5_4():
    table = np.chararray((4,4))
    k=2
    res=tobetested.random_fill_sparse(table, k)
    assert np.where(res == 'vive')
        
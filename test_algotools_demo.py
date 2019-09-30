#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:44:54 2019

@author: alben
"""

import pytest
import S1_algotools_teacherdemo as tobetested

'''
def test_average_above_zero_working1():
	tab_list=[1,2,3,-4,6,-9]
	test, lastID=tobetested.average_above_zero(tab_list)
	assert test==3
	

def inc_(x):
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
        
def test_exo1_1():
    tab=[1,2,3,4,5,6]
    som=tobetested.average_above_zero(tab)
    assert som==3.5
    

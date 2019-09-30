#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:44:54 2019

@author: alben
"""
import S1_algotools_teacherdemo as tobetested
import pytest


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

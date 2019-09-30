#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:44:54 2019

@author: alben
"""

import pytest

def inc_(x):
    return x+1

def test_inc():
    assert inc(3)==5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1/0
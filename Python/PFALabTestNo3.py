# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 20:22:10 2022

@author: SinVas
"""

def facR(n):
    if n == 1:
        return n
    else:
        return n*facR(n - 1)

facR(4)
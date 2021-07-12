# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 04:50:53 2021

@author: User
"""
import numpy as np
from matplotlib import pyplot as plt

def linear_regression(x_val, y_val):
    x_val = np.array(x_val)
    y_val = np.array(y_val)
    n = len(x_val)
    sumX = np.sum(x_val)
    sumY = np.sum(y_val)
    sumXX = np.sum(x_val**2)
    sumXY = np.sum(x_val*y_val)
    
    if 0.0 in x_val and 0.0 in y_val: 
        a0 = 0
        a1 = sumXY/sumXX 
    else: 
        a1 = ((n * sumXY) - (sumX*sumY))/((n * sumXX) - (sumX*sumX))
        a0 = (sumY/n) - (a1*(sumX/n))
    
    return a0, a1


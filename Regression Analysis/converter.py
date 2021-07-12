"""
Solution to the Assignment on Regression Problem
Author: Md. Asif Haider
Student ID: 1805112
Date: July 04, 2021
"""

import linear_regression as lr
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import main2 as result


# data input method 
def input_data():
    x_val = []
    y_val = []
    target_file = "data.txt"
    file = open(target_file)
    for i in file:
        entry = i.split(" ")
        x_val.append(1/(float(entry[0])**2))
        y_val.append(1/(float(entry[1])))   
    
    return x_val, y_val

# function for initial plotting
def plot_function(coeffs=[]):
    
    x, y = input_data()

    fig, ax = plt.subplots()
    ax.scatter(x, y, marker='.', c='blue')

    plt.xlim(-1.0, 5)
    plt.ylim(-0.25, 1.5)
    
    ax.axhline(y=0, color='grey')
    ax.axvline(x=0, color='grey')
    
    sns.set_theme(style="darkgrid")
    if len(coeffs):
        x = np.linspace(0, 10, 100)
        y = coeffs[0] + coeffs[1]*x
        ax.plot(x, y, 'red')
    plt.show()
    return x,y
    
    
if __name__ == '__main__':

    
    # plotting the function  data
    x, y = plot_function()
    param1, param2 = lr.linear_regression(x, y) 
    print("a0: " + str(param1))
    print("a1: " + str(param2))
    plot_function([param1, param2])
    a, b = result.print_answer(param1, param2)
    result.plot_function(a, b)
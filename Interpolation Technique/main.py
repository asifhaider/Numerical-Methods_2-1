"""
Solution to the Assignment on Lagrangian Interpolation (incomplete)
Author: Md. Asif Haider
Student ID: 1805112
Date: June 06, 2021
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def file_input():  # sample file input
    pressure = open('input.txt')
    pressure_dict = {}
    next(pressure)
    for i in pressure:
        entry = i.split("\t")
        pressure_dict[int(entry[0])] = int(entry[1])
    pressure.close()
    return pressure_dict


def obtain_x_values(points, target, polynomial_order):
    interpolates = []
    for i in range(len(points) - 1):
        if points[i] < target < points[i + 1]:
            interpolates.append(points[i])
            interpolates.append(points[i + 1])
            if polynomial_order == 1:
                break
            else:
                multiple = int(polynomial_order / 2)
                remainder = (polynomial_order % 2)
                start = i
                end = i + 1
                if remainder == 1:
                    while multiple:
                        start = start - 1
                        end = end + 1
                        interpolates.append(points[start])
                        interpolates.append(points[end])
                        multiple = multiple - 1
                else:
                    while multiple-1:
                        start = start - 1
                        end = end + 1
                        interpolates.append(points[start])
                        interpolates.append(points[end])
                        multiple = multiple - 1
                    if (target - points[start - 1]) <= (points[end + 1] - target):
                        interpolates.append(points[start - 1])
                    else:
                        interpolates.append(points[end + 1])
    interpolates.sort()
    return interpolates


def lagrange_interpolate(x_values, y_values, target, polynomial_order):
    result = 0.0
    for i in range(polynomial_order+1):
        term = y_values[i]
        for j in range(polynomial_order+1):
            if j!=i:
                term = term * ((target - x_values[j])/(x_values[i] - x_values[j]))
        result += term
    return result


def plotGraph(x_values, y_values):
    
    x = np.array(x_values)
    y = np.array(y_values)
    
    # Plotting the graphs
    plt.ylim([-20, 80])  # limiting y axis value
    plt.plot(x, y, color='green', linestyle='dashed', linewidth=3)  # main graph

    # Creating axis
    plt.grid(True, which='both')
    plt.axhline(y=0, color='blue')
    plt.axvline(x=0, color='blue')

    # Labeling axis
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')

    plt.show()


if __name__ == '__main__':
    pressure_dict = file_input()
    case1_x_values = obtain_x_values(list(pressure_dict.keys()), 28, 3)
    case2_x_values = obtain_x_values(list(pressure_dict.keys()), 32, 3)
    print(case1_x_values)
    print(case2_x_values)
    case1_y_values = [pressure_dict[i] for i in case1_x_values]
    case2_y_values = [pressure_dict[i] for i in case2_x_values]
    print(case1_y_values)
    print(case2_y_values)
    print(lagrange_interpolate(case1_x_values, case1_y_values, 28, 3))
    print(lagrange_interpolate(case2_x_values, case2_y_values, 32, 3))
    plotGraph(list(pressure_dict.keys()), list(pressure_dict.values()))



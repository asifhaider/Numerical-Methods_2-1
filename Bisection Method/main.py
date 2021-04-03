"""

Solution to the Assignment on Bisection Method
Author: Md. Asif Haider
Student ID: 1805112
Date: March 19, 2021

"""
import plot as plt
import table
import root

if __name__ == '__main__':

    # plotting the function  data
    plt.plot_function()

    # using bisection method (0.001, 0.25 or 0.01, 0.1)

    lower_range = input('Input the estimated lower bound of the chosen region!\n')
    upper_range = input('Input the estimated upper bound of the chosen region!\n')

    print('The root found by bisection method is: ' + str(
          root.root_by_bisection(float(lower_range), float(upper_range))))
    print("=====================================================")

    # printing data in tabular format

    table.print_table(float(lower_range), float(upper_range))



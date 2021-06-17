"""
Solution to the Assignment on Numerical Integration: Simpson's 1/3rd Rule
Author: Md. Asif Haider
Student ID: 1805112
Date: June 17, 2021
"""

import math
import pandas as pd
from tabulate import tabulate


# function description of velocity-distance relationship of vertical rocket
def function_value(time, velocity=2000, initial_mass=140000, fuel_rate=2100):
    return velocity * math.log(initial_mass / (initial_mass - (time * fuel_rate))) - (9.8 * time)


# simpson's 1/3rd rule for calculating definite integral
def approximate_vertical_distance(sub_intervals, lower_limit=8, upper_limit=30):
    height = (upper_limit - lower_limit) / sub_intervals
    integral = function_value(lower_limit) + function_value(upper_limit)
    for i in range(sub_intervals - 1):
        if i % 2 == 0:
            integral += 4 * (function_value(lower_limit + height * (i + 1)))
        else:
            integral += 2 * (function_value(lower_limit + height * (i + 1)))
    return height * integral / 3


def absolute_relative_error_finder(iteration):
    errors = ['Not Applicable']
    values = []
    for i in range(iteration):
        values.append(str(approximate_vertical_distance(2*(i + 1))))
        errors.append(str(round((math.fabs(
            approximate_vertical_distance(2*(i + 2)) - approximate_vertical_distance(2*(i + 1))) / (
                                     approximate_vertical_distance(2*(i + 2))) * 100), 4)))
    return values, errors


if __name__ == '__main__':
    iterations = int(input("Provide the highest number of sub-intervals: "))
    result = approximate_vertical_distance(2*iterations)
    print(result)
    calculated_values, relative_errors = absolute_relative_error_finder(iterations)
    table = pd.DataFrame(list(zip([i + 1 for i in range(iterations)], calculated_values, relative_errors)),
                         columns=['Number of Iterations', 'Approximate Vertical Distance(meter)',
                                  'Absolute Approximate Relative Error(percentage)'])
    print(tabulate(table, showindex=False, headers=table.columns))

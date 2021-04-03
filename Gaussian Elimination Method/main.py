"""

Solution to the Assignment on Naive Gaussian Elimination Method
Author: Md. Asif Haider
Student ID: 1805112
Date: April 2, 2021

"""

import numpy as np
import gauss_elimination as ge

if __name__ == '__main__':
    print("=====================================")
    print("Welcome To Gaussian Elimination Demo!")
    print("=====================================")
    while True:
        # infinite loop for continuous inputs
        try:
            unknown = int(
                input("\nEnter the number of unknown variables; Press any other character but numbers to exit: \n"))
        except ValueError as v:
            exit("You have successfully exited the program")
        else:
            coefficients = np.zeros((unknown, unknown))
            constants = np.zeros((unknown, 1))
            print("\nEnter the Co-efficient Matrix: ")

            for i in range(unknown):
                try:
                    row = list(map(float, input().split()))
                except ValueError as e:
                    exit("Invalid Input. Please Try Again!")

                for j in range(unknown):
                    try:
                        coefficients[i][j] = row[j]
                    except IndexError or ValueError as e:
                        break
            print("Your Provided Co-efficient Matrix: ")
            print(coefficients)

            print("\nEnter the Constant Matrix")
            for i in range(unknown):
                try:
                    constants[i] = float(input())
                except ValueError or IndexError as e:
                    exit("Invalid Input. Please Try Again!")

            print("Your Provided Constant Matrix: ")
            print(constants)

            roots = ge.GaussianElimination(coefficients, constants)
            if roots is None:
                continue    # division by zero, moving forward
            print('\nThe Solution Matrix: ')
            for i in range(roots.size):
                print(np.around(roots[i], 4))   # allowing four precision decimal values

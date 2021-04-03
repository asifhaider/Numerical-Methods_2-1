import numpy as np


# Naive Gaussian Elimination Algorithm
def GaussianElimination(A, B, d=True):
    # creating augmented matrix for easy calculation
    augmented_matrix = np.concatenate((A, B), axis=1)
    # print("The Concatenated Augmented Matrix: ")
    # print(augmented_matrix)
    n = B.size

    # Forward Elimination Step
    for i in range(n):
        # pivot point co-efficient can't be zero to avoid division by zero
        if augmented_matrix[i][i] == 0.0:
            print("\nDivision By Zero Encountered. Please Try Again!")
            return None
        for j in range(i + 1, n):
            multiplying_factor = augmented_matrix[j][i] / augmented_matrix[i][i]
            # print("Multiplied by", multiplying_factor)
            # augmented matrix column no is row+1
            for k in range(n + 1):
                augmented_matrix[j][k] = augmented_matrix[j][k] - multiplying_factor * augmented_matrix[i][k]
            if d:
                # parsing out two input matrices from the augmented one
                print("\nMatrix A After a Single Operation: ")
                print(augmented_matrix[:, 0:n])
                print("Matrix B After a Single Operation: ")
                print(augmented_matrix[:, -1].reshape(-1, 1))

    # Backward Substitution Step
    X = np.zeros(n)
    X[n - 1] = augmented_matrix[n - 1][n] / augmented_matrix[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        temp = augmented_matrix[i][-1]
        for j in range(i + 1, n):
            temp = temp - augmented_matrix[i][j] * X[j]
        # dividing with the pivot co-efficient to find and assign the latest root
        X[i] = temp / augmented_matrix[i][i]

    return X

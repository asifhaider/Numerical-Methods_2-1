import pandas as pd
import bisection as bs


def print_table(lower_bound, upper_bound, error_tolerance=0.0, max_iter=20):
    # error tolerance is not applicable here, only 20 iterations matter
    # placeholder used to cancel out the final root

    _, error_values, estimated_roots = bs.bisection_algorithm(lower_bound, upper_bound, error_tolerance, max_iter)
    rows = list()
    for i in range(len(error_values)):
        text = 'Iteration ' + str(i+1) + ':'
        rows.append(text)
    # displaying the data with the help of data frame
    df = pd.DataFrame(list(zip(error_values, estimated_roots)),
                      index=rows, columns=['Absolute Relative Approximate Errors', 'Estimated Roots'])
    print(df)

import math
import plot


def find_mid(lower, upper):
    # returning the estimated root (middle point)
    return (lower + upper)/2


def compare(lower, upper):
    # comparing the function value in upper and lower bounds
    return plot.mole_fraction_function(lower) * plot.mole_fraction_function(upper)


def bisection_algorithm(lower_bound, upper_bound, error_tolerance, max_iter):
    iteration = 0
    error_values = list()
    estimated_roots = list()
    while True:
        if iteration == max_iter:
            break
        old_mid = find_mid(lower_bound, upper_bound)
        if compare(lower_bound, old_mid) > 0:
            lower_bound = old_mid
            # fixing the new bound
        elif compare(lower_bound, old_mid) < 0:
            upper_bound = old_mid
            # fixing the new bound
        else:
            root = old_mid
            # expected root found
            break
        new_mid = find_mid(lower_bound, upper_bound)
        # assigning the new estimated root for next iteration
        try:
            # new midpoint might be zero, so handling this
            rel_approximate_error = math.fabs((new_mid - old_mid) / new_mid)
            error_values.append(rel_approximate_error)
        except ZeroDivisionError:
            print('Not Applicable')
            rel_approximate_error = 1
            # manually assigning undefined case to 100% error
            error_values.append(rel_approximate_error)

        root = new_mid
        estimated_roots.append(root)
        iteration += 1
        if rel_approximate_error < error_tolerance:
            break

    return root, error_values, estimated_roots


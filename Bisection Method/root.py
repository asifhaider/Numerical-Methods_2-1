import bisection as bs


def root_by_bisection(lower_bound, upper_bound, error_tolerance=0.005, max_iter=20):
    # using error tolerance to find out the root
    # once it will achieve expected accuracy, it will not ignore the maximum iteration number
    # placeholders are used to consider the root only

    root, _, _ = bs.bisection_algorithm(lower_bound, upper_bound, error_tolerance, max_iter)
    return root

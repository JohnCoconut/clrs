def max_subarray(a):
    max_ending_here = max_so_far = a[0]
    print("{:<10}{:<10}".format(max_ending_here, max_so_far))
    for x in a[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
        print("{:<10}{:<10}".format(max_ending_here, max_so_far))
    return max_so_far

a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_subarray(a)

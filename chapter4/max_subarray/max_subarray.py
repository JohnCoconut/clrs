def max_subarray(a, low, high):
    if low == high:
        return (low, high, a[low])
    else:
        mid = (low + high) // 2
        (l_low, l_high, l_sum) = max_subarray(a, low, mid)
        (r_low, r_high, r_sum) = max_subarray(a, mid+1, high)
        (c_low, c_high, c_sum) = max_cross_subarray(a, low, mid, high)
        if l_sum >= r_sum and l_sum >= c_sum:
            return (l_low, l_high, l_sum)
        elif r_sum >= l_sum and r_sum >= c_sum:
            return (r_low, r_high, r_sum)
        else:
            return (c_low, c_high, c_sum)

def max_cross_subarray(a, low, mid, high):
    i, j = mid, mid + 1
    s = 0
    l_sum = a[mid] - 1
    r_sum = a[mid + 1] - 1
    while i >= low:
        s += a[i]
        if s >= l_sum:
            l_sum = s
            max_left = i
        i -= 1
    s = 0
    while j <= high:
        s += a[j]
        if s >= r_sum:
            r_sum = s
            max_right = j
        j += 1
    return (max_left, max_right, l_sum + r_sum)

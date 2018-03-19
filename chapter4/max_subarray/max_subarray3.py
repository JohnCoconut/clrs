def max_subarray3(a):
    size = len(a) + 1
    s = a[0]
    for i in range(size):
        for j in range(i+1, size):
            loop_s = sum(a[i:j])
            if loop_s > s:
                s = loop_s
                left = i
                right = j - 1
    return (left, right, s)

def max_subarray2(a):
    length = len(a)
    maxsofar = a[0] - 1
    left = 0
    while left < length:
        max = 0
        right = left
        while right < length:
            max += a[right]
            if max > maxsofar:
                maxsofar = max
                l = left
                r = right
            right += 1
        left += 1
    return (l, r, maxsofar)

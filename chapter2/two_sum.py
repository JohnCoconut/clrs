def two_sum(l, value):
    merge_sort(l, 0, len(l)-1)
    left, right = 0, len(l) - 1
    while left < right:
        if l[left] + l[right] == value:
            return (left, right)
        elif l[left] + l[right] < value:
            left += 1
        else:
            right -= 1
    return None

def merge_sort(l, p, r):
    if p < r:
        q = (p + r) // 2;
        merge_sort(l, p, q)
        merge_sort(l, q+1, r)
        merge(l, p, q, r)

def merge(l, p, q, r):
    l1 = l[p:q+1]
    l2 = l[q+1:r+1]
    n1 = q - p + 1
    n2 = r - q
    i, j, k = 0, 0, p
    while i < n1 and j < n2:
        if l1[i] < l2[j]:
            l[k] = l1[i]
            i += 1 
        else:
            l[k] = l2[j]
            j += 1
        k += 1
    if i == n1:
        while k <= r:
            l[k] = l2[j]
            j += 1
            k += 1
    if j == n2:
        while k <= r:
            l[k] = l1[i]
            i += 1
            k += 1

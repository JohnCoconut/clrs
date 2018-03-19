def merge_sort2(l, p, r):
    # p, r must be in li
    if r - p > 10:
        q = (p + r) // 2
        merge_sort2(l, p, q)
        merge_sort2(l, q+1, r)
        merge(l, p, q, r)
    else:
        insertion_sort(l, p, r)

def merge(l, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    l1 = l[p:q+1]
    l2 = l[q+1:r+1]
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
            k += 1
            j += 1
    if j == n2:
        while k <= r:
            l[k] = l1[i]
            k += 1
            i += 1

def insertion_sort(l,p, r):
    j = p + 1
    while j <= r:
        key = l[j]
        i = j - 1
        while i >= p and l[i] > key:
            l[i+1] = l[i]
            i -= 1
        l[i+1] = key
        j += 1

def insertion_sort(li, j):
    if j == 0:
        return
    else:
        insertion_sort(li, j - 1)
        key = li[j]
        i = j - 1
        while i >= 0 and li[i] > key:
            li[i + 1] = li[i]
            i -= 1
        li[i + 1] = key

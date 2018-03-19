def insertion_sort_decreasing(li):
    assert isinstance(li, list)
    j = 1
    length = len(li)
    while j < length:
        key = li[j]
        i = j - 1
        while i >= 0 and li[i] < key:
            li[i + 1] = li[i]
            i -= 1
        li[i + 1] = key
        j += 1
    return li

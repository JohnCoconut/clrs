def linear_search(li, v):
    length = len(li)
    i = 0
    while i < length and li[i] != v:
        i += 1
    return i if i < length else None

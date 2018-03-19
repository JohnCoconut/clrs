def insertion_sort(li):
    assert isinstance(li, list)
    length = len(li)
    j = 1
    while j < length:
        key = li[j]
        i = j - 1
        while li[i] > key and i >= 0:
            li[i+1] = li[i]
            i -= 1
        li[i+1] = key
        j += 1

if __name__ == "__main__":
    ''' use unittest'''
    pass

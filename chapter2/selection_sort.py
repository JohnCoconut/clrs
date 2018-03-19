def selection_sort(li):
    length = len(li)
    j = 0
    while j < length - 1:
        key = j
        i = j + 1
        while i < length:
            if li[i] < li[j]:
                key = i
            i += 1
        li[j], li[key] = li[key], li[j]
        j += 1
    return li

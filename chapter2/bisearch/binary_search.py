def binary_search(l, low, high, value):
    if low <= high:
        mid = (low + high) // 2
        if l[mid] == value:
            return mid
        elif l[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
        return binary_search(l, low, high, value)
    else:
        return None

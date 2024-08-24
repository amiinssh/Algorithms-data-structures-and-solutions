def monotonic_array(array):

    n = len(array)
    if n == 0:
        return True
    first = array[0]
    last = array[-1]

    if first > last:
        for k in range(n - 1):
            if array[k] < array[k + 1]:
                return False

    elif first == last:
        for k in range(n - 1):
            if array[k] != array[k + 1]:
                return False

    else:
        for k in range(n - 1):
            if array[k] > array[k + 1]:
                return False

    return True

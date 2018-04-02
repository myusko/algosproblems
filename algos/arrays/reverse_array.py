def reverse_array(arr):
    if not isinstance(arr, list):
        return None
    l = len(arr)
    if l == 1:
        return arr
    for x in range(l - 1, 0, -1):
        for i in range(x):
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp
    return arr

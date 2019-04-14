def bubble_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    arr_len = len(arr)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for x in range(arr_len - 1):
            if arr[x] > arr[x + 1]:
                hold = arr[x + 1]
                arr[x + 1] = arr[x]
                arr[x] = hold
                is_sorted = False
    return arr

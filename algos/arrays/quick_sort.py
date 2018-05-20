def quick_sort(arr):
    sorted_ = False
    c = len(arr[1:len(arr) - 1])
    while not sorted_:
        sorted_ = True
        for x in range(c):
            if arr[x] > arr[x + 1]:
                temp = arr[x + 1]
                arr[x + 1] = arr[x]
                arr[x] = temp
                sorted_ = False
    return arr

print(quick_sort([4, 5, 3, 7, 2]))

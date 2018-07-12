def find_maximum(arr):
    max_value = arr[0]
    min_value = arr[0]
    for x in range(len(arr) - 1):
        if max_value < arr[x + 1]:
            max_value = arr[x + 1]
        if min_value > arr[x + 1]:
            min_value = arr[x + 1]
    return '{} {}'.format(max_value, min_value)

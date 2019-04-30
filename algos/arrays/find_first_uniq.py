def find_first_uniq(arr):
    if len(arr) == 0:
        return arr
    elif len(arr) == 1:
        return arr[0]
    count = 0
    for x in range(len(arr) - 1):
        if arr[x] == arr[x + 1]:
            count += 1
            if count == 2:
                break
            return arr[x]

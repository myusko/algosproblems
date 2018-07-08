def find_min(arr):
    for x in range(len(arr) - 1):
        if arr[x] < arr[x + 1]:
            return arr[x]
        else:
            return arr[x + 1]


def minimum_of_two(arr):
    result = []
    for x in range(len(arr)):
        if isinstance(arr[x], list):
            min_value = find_min(arr[x])
            result.append(min_value)
    output = ' '.join(list(map(str, result)))
    return output

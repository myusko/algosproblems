def find_minimum(arr):
    length = len(arr)
    for x in range(len(arr) - length + 1):
        a, b, c = arr[x], arr[x + 1], arr[x + 2]
        if a < b and a < c:
            return a
        if b < a and b < c:
            return b
        else:
            return c


def minimum_of_three(arr):
    result = []
    for x in arr:
        result.append(find_minimum(x))
    output = ' '.join(list(map(str, result)))
    return output

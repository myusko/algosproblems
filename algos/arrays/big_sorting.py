# Solution one, bad complexity and didn't passing all test cases
def big_sorting(unsorted):
    is_sorted = False
    length = len(unsorted)
    while not is_sorted:
        is_sorted = True
        for x in range(length - 1):
            if len(unsorted[x]) > len(unsorted[x + 1]):
                temp = unsorted[x + 1]
                unsorted[x + 1] = unsorted[x]
                unsorted[x] = temp
                is_sorted = False
    return unsorted


# Solution two, passed all test cases
def big__sorting(unsorted):
    return sorted(sorted(unsorted), key=len)

print(big__sorting(['5', '10', '3333']))
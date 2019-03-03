"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.
"""


def find_numbers(arr):
    if len(arr) == 1:
        return arr
    unique_numbers = set(arr)
    array_length = len(arr) + 1
    result = []
    for x in range(1, array_length):
        if x not in unique_numbers:
            result.append(x)
    return result

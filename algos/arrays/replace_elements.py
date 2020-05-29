"""
Given an array arr, replace every element in that array with the greatest element among
the elements to its right, and replace the last element with -1.

After doing so, return the array.
"""


def replace_elements(array):
    for i in range(len(array) - 1):
        array[i] = max(array[i + 1:])
    array[-1] = -1
    return array

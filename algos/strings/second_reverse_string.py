"""
Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.
"""


def reverse_string(arr):
    for x in range(len(arr)):
        arr.insert(x, arr.pop())
    # NOTE: return statement is only for test purposes.
    return arr

"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist,
return the maximum number. The time complexity must be in O(n).
"""


def third_maximum(nums):
    new_list = list(set(nums))

    if len(new_list) < 3:
        return max(nums)

    for _ in range(2):
        del new_list[new_list.index(max(new_list))]
    return max(new_list)

"""
Given an array of integers, find if the array contains any duplicates.
"""


def contains_duplicate(nums):
    return len(nums) != len(set(nums))

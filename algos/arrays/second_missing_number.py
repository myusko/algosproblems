"""
Given an array containing n distinct numbers
taken from 0, 1, 2, ..., n, find the one that is missing from the array.
"""


def find_missing(nums):
    num_set = set(nums)
    n = len(nums) + 1
    for number in range(n):
        if number not in num_set:
            return number

# Given an list containing 9 numbers ranging from 1 to 10,
# write a function to find the missing number.
# Assume you have 9 numbers between 1 to 10 and only one number is missing.


def find_missing_number(list_numbers):
    n = len(list_numbers)
    total = (n + 1) * (n + 2) / 2
    total_sum = sum(list_numbers)
    return total - total_sum

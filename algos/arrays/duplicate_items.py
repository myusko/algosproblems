# Write a function - duplicate_items to find the redundant or repeated items
# in a list and return them in sorted order.
# This method should return a list of redundant integers in ascending sorted order.


def duplicate_items(list_numbers):
    counts = {x: list_numbers.count(x) for x in list_numbers}
    unique = [key for key, value in counts.items() if value > 1]
    return sorted(unique)

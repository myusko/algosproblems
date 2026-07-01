# Write a function, tree_min_value, that takes in the root of a binary tree that contains number values.
# The function should return the minimum value within the tree. You may assume that the input tree is non-empty.

import math


def tree_min_value_recursive(root):
    def minimum_value(root, min_value):
        if root is None:
            return min_value

        min_value = min(root.val, min_value)
        return min(
            minimum_value(root.left, min_value), minimum_value(root.right, min_value)
        )

    result = minimum_value(root, math.inf)
    return result


def tree_min_value(root):
    min_value = math.inf
    stack = [root]

    while stack:
        current = stack.pop()
        min_value = min(min_value, current.val)

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return min_value

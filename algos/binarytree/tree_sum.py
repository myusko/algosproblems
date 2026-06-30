# Write a function, tree_sum, that takes in the root of a binary tree that contains number values.
# The function should return the total sum of all values in the tree.


def tree_sum_recursion(root):
    if not root:
        return 0

    left_sum = tree_sum(root.left)
    right_sum = tree_sum(root.right)

    return root.val + left_sum + right_sum


def tree_sum(root):
    queue = [root]
    result = 0

    while queue:
        current = queue.pop(0)

        if current:
            result += current.val

        if current and current.left:
            queue.append(current.left)

        if current and current.right:
            queue.append(current.right)

    return result

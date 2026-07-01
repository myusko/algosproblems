# Write a function, tree_includes, that takes in the root of a binary tree and a target value.
# The function should return a boolean indicating whether or not the value is contained in the tree.


def tree_includes_recursive(root, target):
    if not root:
        return False

    if root.val == target:
        return True

    return tree_includes_recursive(root.left, target) or tree_includes_recursive(
        root.right, target
    )


def tree_includes(root, target):
    queue = [root]

    while queue:
        current = queue.pop(0)
        if not current:
            continue

        if current.val == target:
            return True

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)
    return False

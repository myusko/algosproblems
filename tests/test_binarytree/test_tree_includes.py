from algos.binarytree.tree_includes import tree_includes_recursive, tree_includes

import pytest
from typing import Any


class BinaryTree:
    def __init__(
        self,
        val: Any,
        left: "None | BinaryTree" = None,
        right: "None | BinaryTree" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


@pytest.mark.parametrize(
    "function",
    [
        tree_includes,
        tree_includes_recursive,
    ],
)
def test_binary_tree_includes_true(function):
    tree = BinaryTree(1)
    tree2 = BinaryTree(2)
    tree3 = BinaryTree(3)
    tree.left = tree2
    tree.right = tree3

    assert function(tree, 3)


@pytest.mark.parametrize(
    "function",
    [
        tree_includes,
        tree_includes_recursive,
    ],
)
def test_binary_tree_include_false(function):
    tree = BinaryTree(1)
    tree2 = BinaryTree(2)
    tree3 = BinaryTree(3)
    tree.left = tree2
    tree.right = tree3

    assert not function(tree, 5)

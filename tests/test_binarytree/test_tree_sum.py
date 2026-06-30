from algos.binarytree.tree_sum import tree_sum, tree_sum_recursion
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
        tree_sum,
        tree_sum_recursion,
    ],
)
def test_binary_tree_sum(function):
    tree = BinaryTree(1)
    tree2 = BinaryTree(2)
    tree3 = BinaryTree(3)
    tree.left = tree2
    tree.right = tree3

    assert function(tree) == 6

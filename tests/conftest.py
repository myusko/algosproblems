from typing import Any

import pytest


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


@pytest.fixture
def simple_binary_tree() -> BinaryTree:
    tree = BinaryTree(1)
    tree2 = BinaryTree(2)
    tree3 = BinaryTree(3)
    tree.left = tree2
    tree.right = tree3

    return tree


@pytest.fixture
def empty_binary_tree() -> BinaryTree:
    return BinaryTree(None)

from algos.binarytree.tree_includes import tree_includes_recursive, tree_includes

import pytest


@pytest.mark.parametrize(
    "function",
    [
        tree_includes,
        tree_includes_recursive,
    ],
)
def test_binary_tree_includes_true(function, simple_binary_tree):
    assert function(simple_binary_tree, 3)


@pytest.mark.parametrize(
    "function",
    [
        tree_includes,
        tree_includes_recursive,
    ],
)
def test_binary_tree_include_false(function, simple_binary_tree):
    assert not function(simple_binary_tree, 5)

from algos.binarytree.tree_min_value import tree_min_value_recursive, tree_min_value
import pytest


@pytest.mark.parametrize(
    "function",
    [
        tree_min_value_recursive,
        tree_min_value,
    ],
)
def test_binary_tree_sum(function, simple_binary_tree):
    assert function(simple_binary_tree) == 1

from algos.binarytree.tree_sum import tree_sum, tree_sum_recursion
import pytest


@pytest.mark.parametrize(
    "function",
    [
        tree_sum,
        tree_sum_recursion,
    ],
)
def test_binary_tree_sum(function, simple_binary_tree):
    assert function(simple_binary_tree) == 6

from algos.arrays.shuffle_the_array import shuffle
import pytest


@pytest.mark.parametrize(
    'data, n, expected',
    [
        ([2, 5, 1, 3, 4, 7], 3, [2, 3, 5, 4, 1, 7]),
        ([1, 2, 3, 4, 4, 3, 2, 1], 4, [1, 4, 2, 3, 3, 2, 4, 1]),
        ([1, 1, 2, 2], 2, [1, 2, 1, 2])
    ]
)
def test_shuffle_the_array(data, n, expected):
    assert shuffle(data, n) == expected

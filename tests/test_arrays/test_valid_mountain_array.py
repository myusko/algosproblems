import pytest

from algos.arrays.valid_mountain_array import valid_mountain_array


@pytest.mark.parametrize(
    'data,expected',
    [
        ([2, 1], False),
        ([3, 5, 5], False),
        ([0, 3, 2, 1], True),
        ([0, 1, 2, 3, 4, 5, 4, 3, 2, 1], True)
    ]
)
def test_valid_mountain_array(data, expected):
    assert valid_mountain_array(data) == expected

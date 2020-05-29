import pytest

from algos.arrays.replace_elements import replace_elements


@pytest.mark.parametrize(
    'data,expected', [([17, 18, 5, 4, 6, 1], [18, 6, 6, 6, 1, -1])]
)
def test_replace_elements(data, expected):
    assert replace_elements(data) == expected

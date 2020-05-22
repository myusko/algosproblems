import pytest

from algos.strings.frequency_sort import frequency_sort


@pytest.mark.parametrize(
    'data, expected', [("tree", "eetr"), ("cccaaa", "cccaaa"), ("Aabb", "bbAa"), ("", "")]
)
def test_frequency_sort(data, expected):
    assert frequency_sort(data) == expected

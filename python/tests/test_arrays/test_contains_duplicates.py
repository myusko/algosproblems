from algos.arrays.contains_duplicate import contains_duplicate


def test_contains_duplicate():
    assert contains_duplicate([3, 1]) is False
    assert contains_duplicate([1, 2, 1, 5]) is True
    assert contains_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 1, 1]) is True

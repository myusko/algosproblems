from algos.arrays.second_missing_number import find_missing


def test_find_missing():
    assert find_missing([0, 1, 3, 4]) == 2
    assert find_missing([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8

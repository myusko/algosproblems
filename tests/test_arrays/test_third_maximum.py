from algos.arrays.third_maximum import third_maximum


def test_third_maximum():
    assert third_maximum([3, 2, 1]) == 1
    assert third_maximum([2, 1]) == 2
    assert third_maximum([2, 2, 3, 1]) == 1


from algos.arrays.minimum_of_three import find_minimum, minimum_of_three


def test_find_minimum():
    assert 1 == find_minimum([1, 20, 11, 22, 55])


def test_find_minimum_of_three():
    data = [
        [-9155969, 8094769, 6063935],
        [-901045, 3239312, 2616666],
        [-8451454, 7226886, 7796624],
    ]
    assert '-9155969 -901045 -8451454' == (minimum_of_three(data))

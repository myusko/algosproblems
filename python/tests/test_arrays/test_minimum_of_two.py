from algos.arrays.minimum_of_two import minimum_of_two, find_min


def test_find_min():
    assert (1, 0) == (find_min([1, 2]), find_min([3, 0]))


def test_minimum_of_two():
    data = [
        [-5517365, 9888247],
        [-9929276, -4320364],
        [-8783781, -3396733]
    ]

    assert "-5517365 -9929276 -8783781" == minimum_of_two(data)

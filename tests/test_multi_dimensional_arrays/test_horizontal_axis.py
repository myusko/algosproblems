from algos.multi_dimensional_arrays.horizontal_flip import flip_horizontal_axis


def test_horizontal_axis():
    data_one = flip_horizontal_axis([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    data_two = flip_horizontal_axis([[1]])
    data_third = flip_horizontal_axis([[1, 0, 0], [0, 0, 1]])

    assert (data_one, data_two, data_third) == ([[7, 8, 9], [4, 5, 6], [1, 2, 3]],
                                                [[1]],
                                                [[0, 0, 1], [1, 0, 0]])

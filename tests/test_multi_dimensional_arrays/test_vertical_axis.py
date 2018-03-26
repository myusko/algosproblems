from algos.multi_dimensional_arrays.vertical_flip import flip_vertical_axis


def test_vertical_flip():
    data_one = flip_vertical_axis([[0, 1]])
    data_two = flip_vertical_axis([[1, 0, 1], [1, 0, 1]])
    data_third = flip_vertical_axis([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert (data_one, data_two, data_third) == ([[1, 0]], [[1, 0, 1], [1, 0, 1]],
                                                [[3, 2, 1], [6, 5, 4], [9, 8, 7]])

from algos.multi_dimensional_arrays.transpose_matrix import transpose_matrix


def test_transpose_matrix():
    data_one = transpose_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    data_two = transpose_matrix([[1, 0, 1], [1, 0, 1], [1, 0, 1]])
    data_third = transpose_matrix([[1]])
    assert (data_one, data_two, data_third) == ([[1, 4, 7], [2, 5, 8], [3, 6, 9]],
                                                [[1, 1, 1], [0, 0, 0], [1, 1, 1]],
                                                [[1]])

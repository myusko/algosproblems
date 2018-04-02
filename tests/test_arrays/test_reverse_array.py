from algos.arrays.reverse_array import reverse_array


def test_reverse_array():
    data_one = reverse_array('bad type')
    data_two = reverse_array([1])
    data_third = reverse_array([1, 2, 3, 4, 5, 6])
    assert (data_one, data_two, data_third) == (None, [1], [6, 5, 4, 3, 2, 1])

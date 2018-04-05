from algos.arrays.bubble_sort import bubble_sort


def test_bubble_sort():
    data_one = bubble_sort([4, 3, 2, 10])
    data_two = bubble_sort([1])
    data_third = bubble_sort([])
    assert (data_one, data_two, data_third) == ([2, 3, 4 , 10], [1], [])

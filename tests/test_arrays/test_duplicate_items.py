from algos.arrays.duplicate_items import duplicate_items


def test_duplicate_items():
    first_data = duplicate_items([1, 1, 2, 4])
    second_data = duplicate_items([2, 3, 2, 1, 1])
    third_data =  duplicate_items([1, 2, 3, 4])
    assert (first_data, second_data, third_data) == ([1], [1, 2], [])

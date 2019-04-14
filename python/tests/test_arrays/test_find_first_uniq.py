from algos.arrays.find_first_uniq import find_first_uniq


def test_first_unique():
    first_data = find_first_uniq(['A', 'B', 'C', 'C', 'D', 'D'])
    second_data = find_first_uniq([])
    third_data = find_first_uniq(['A'])
    assert (first_data, second_data, third_data) == ('C', [], 'A')

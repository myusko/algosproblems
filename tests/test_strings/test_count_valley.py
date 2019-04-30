from algos.strings.count_valleys import count_valley


def test_count_valley():
    data_one = count_valley('UDDDUDUU')
    data_two = count_valley('DDUUDDUDUUUD')
    assert (data_one, data_two) == (1, 2)

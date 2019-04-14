from algos.arrays.big_sorting import big_sorting, big__sorting


def test_big_sorting():
    data_one = big__sorting(['10', '5', '3333'])
    data_two = big_sorting(['11', '5', '3333'])
    assert (data_one, data_two) == (['5', '10', '3333'], ['5', '11', '3333'])

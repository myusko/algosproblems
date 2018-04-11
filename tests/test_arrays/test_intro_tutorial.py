from algos.arrays.intro_to_tutorial_challenges import intro_tutorial


def test_intro_tutorial():
    data_one = intro_tutorial(3, [5, 10, 3])
    data_two = intro_tutorial(4, [11, 4])
    assert (data_one, data_two) == (2, 1)

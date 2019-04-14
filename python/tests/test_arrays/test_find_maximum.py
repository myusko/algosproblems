from algos.arrays.find_maximum import find_maximum


def test_find_maximum():
    data = [
        -51022, 1145, -48989, 47088,
        -64165, 61139, 32121, 65132,
        -56351, 10034, 13233, 12323
    ]
    assert find_maximum(data) == '65132 -64165'

from algos.strings.hackerrank_string import hackerrank_in_string


def test_hackerrank_in_string():
    data_one = hackerrank_in_string('hereiamstackerrank')
    data_two = hackerrank_in_string('hackerworld')
    assert (data_one, data_two) == ('YES', 'NO')

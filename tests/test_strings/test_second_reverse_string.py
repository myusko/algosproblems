from algos.strings.second_reverse_string import reverse_string


def test_second_reverse_string():
    expected = ['o', 'l', 'l', 'e', 'h']
    actual = reverse_string(['h', 'e', 'l', 'l', 'o'])
    assert actual == expected

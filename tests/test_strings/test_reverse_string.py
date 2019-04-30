from algos.strings.reverse_string import reverse_string


def test_reverse_string():
    data_one = reverse_string('1')
    data_two = reverse_string('madam')
    data_third = reverse_string('Programming')
    assert (data_one, data_two, data_third) == ('1', 'madam', 'gnimmargorP')

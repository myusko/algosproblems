from algos.strings.is_pangram import is_pangram, is__pangram


def test_is_pangram():
    data_one = is__pangram('We promptly judged antique ivory buckles for the next prize')
    data_two = is_pangram('Hello')
    assert (data_one, data_two) == ('pangram', 'not pangram')

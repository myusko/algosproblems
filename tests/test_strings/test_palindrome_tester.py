from algos.strings.palindrome_tester import is_palindrome


def test_is_palindrome():
    data_one = is_palindrome('Apple')
    data_two = is_palindrome('hello')
    data_third = is_palindrome('madam')
    assert (data_one, data_two, data_third) == (False, False, True)

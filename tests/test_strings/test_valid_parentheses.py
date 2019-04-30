from algos.strings.valid_parentheses import valid_parentheses


def test_valid_parentheses():
    data_one = valid_parentheses('((')
    data_two = valid_parentheses('[][]{}()[]')
    data_third = valid_parentheses('(){}[}')
    assert (data_one, data_two, data_third) == (False, True, False)

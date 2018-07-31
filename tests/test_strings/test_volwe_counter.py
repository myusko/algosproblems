from algos.strings.count_volwes import vowel_counter


def test_volwe_counter():
    data = [
        'abracadabra',
        'pear tree',
        'o a kak ushakov lil vo kashu kakao',
        'my pyx'
    ]
    result = vowel_counter(data)
    assert result == '5 4 13 2'

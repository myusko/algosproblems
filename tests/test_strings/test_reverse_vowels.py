from algos.strings.reverse_vowels import reverse_vowels


def test_reverse_vowels():
    assert reverse_vowels("hello") == "holle"
    assert reverse_vowels("olli") == "illo"
    assert reverse_vowels("helloworld") == "hollowerld"

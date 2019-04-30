from algos.strings.ransom_note import ransom


def test_ransom_note():
    assert ransom('a', 'b') is False
    assert ransom('aa', 'bb') is False
    assert ransom('aa', 'aab') is True
    assert ransom('abaa', 'abbaa') is True

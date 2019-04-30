from algos.arrays.keyboard_row import keyboard_row


def test_keyboard_row():
    assert keyboard_row(["Hello", "Alaska", "Dad", "Peace"]) == ['Alaska', 'Dad']
    assert keyboard_row(['qwert', 'secondword']) == ['qwert']


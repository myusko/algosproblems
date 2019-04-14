from algos.strings.student_attendance import student_attendance


def test_studante_attendance():
    assert student_attendance('PPALLP') is True
    assert student_attendance('PPALLL') is False

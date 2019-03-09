"""
Given a List of words, return the words that can be typed using letters of alphabet
on only one row's of American keyboard like the image below.
"""


def keyboard_row(words):
    result = []
    first_row = set('qwertyuiop')
    second_row = set('asdfghjkl')
    third_row = set('zxcvbnm')
    for word in words:
        if set(word.lower()).issubset(first_row) \
                or set(word.lower()).issubset(second_row) \
                or set(word.lower()).issubset(third_row):
            result.append(word)
    return result

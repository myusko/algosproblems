"""
Write a function that takes a string as input and reverse only the vowels of a string.
"""


def reverse_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    pos = []
    for c in s:
        if c in vowels:
            pos.append(c)
    converted = list(s)
    for x in range(len(converted)):
        if converted[x] in vowels:
            converted[x] = pos.pop()
    return "".join(c for c in converted)

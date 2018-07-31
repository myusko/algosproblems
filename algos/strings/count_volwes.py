from collections import OrderedDict


def count_letter(word):
    vowels = ['a', 'o', 'u', 'i', 'e', 'y']
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count


def vowel_counter(arr):
    result = OrderedDict((letter, count_letter(letter)) for letter in arr)
    return ' '.join(str(value) for value in result.values())

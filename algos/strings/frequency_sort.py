"""
Given a string, sort it in decreasing order based on the frequency of characters.

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
"""


# Time complexity is O(n)
def frequency_sort(s):
    char_count = {}
    result = ''
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    sorted_ = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

    for char, times in sorted_:
        result += char * times
    return result

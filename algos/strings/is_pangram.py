import string

# The first solution, all tests passed
def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    s_ = set(s.lower())
    if all((c in s_) for c in alphabet):
        return 'pangram'
    return 'not pangram'


# The second solution, all tests passed
def is__pangram(s):
    alphabet = set(string.ascii_lowercase)
    alphabet_length = len(alphabet)
    s_ = set(s.lower())
    count = 0
    for x in alphabet:
        if x in s_:
            count += 1
            if count == alphabet_length:
                return 'pangram'
    return 'not pangram'

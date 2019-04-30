def hackerrank_in_string(s):
    pos = 0
    template = 'hackerrank'
    for word in template:
        if word in s[pos:]:
            pos = s.index(word, pos) + 1
        else:
            return 'NO'
    return 'YES'

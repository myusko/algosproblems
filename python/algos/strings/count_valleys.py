# https://www.hackerrank.com/challenges/counting-valleys/problem


def count_valley(s):
    level = valley = 0
    for x in s:
        if x == 'U':
            level += 1
        else:
            level -= 1
        if x == 'U' and level == 0:
            valley += 1
    return valley

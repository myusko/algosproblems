"""
FizzBuzz
Write a program that outputs the string representation of numbers from 1 to n.
"""


def is_buzz(n):
    if int(n) % 3 == 0 and int(n) % 5 == 0:
        return "FizzBuzz"
    elif int(n) % 3 == 0:
        return "Fizz"
    elif int(n) % 5 == 0:
        return "Buzz"
    return n


def fizz_buzz(n):
    converted = list(map(lambda x: str(x), range(1, n + 1)))
    result = [is_buzz(x) for x in converted]
    return result

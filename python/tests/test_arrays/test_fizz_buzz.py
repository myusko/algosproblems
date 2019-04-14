from algos.arrays.fizz_buzz import fizz_buzz


def test_fizz_buzz():
    expected = [
        "1", "2", "Fizz", "4", "Buzz",
        "Fizz", "7", "8", "Fizz",
        "Buzz", "11", "Fizz",
        "13", "14", "FizzBuzz"
    ]
    assert fizz_buzz(15) == expected

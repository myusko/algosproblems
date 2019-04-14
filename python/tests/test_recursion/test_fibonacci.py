from algos.recursion.fibonacci import fib


def test_fibonacci():
    data_one = fib(0)
    data_two = fib(10)
    data_third = fib(1)
    assert (data_one, data_two, data_third) == (0, 55, 1)

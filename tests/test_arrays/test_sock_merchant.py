from algos.arrays.sock_merchant import sock_merchant


def test_sock_merchant():
    data_one = sock_merchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
    assert data_one == 3

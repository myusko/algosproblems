from data_structures.linked_list import LinkedList


def test_double_linked_list():
    linked_list = LinkedList()
    prepared_list = list(range(1, 10))

    for x in range(1, 10):
        linked_list.append(x)

    assert linked_list.all() == prepared_list
    assert linked_list.maximum() == max(prepared_list)
    assert linked_list.minimum() == min(prepared_list)
    assert linked_list.reverse() == list(reversed(prepared_list))

    assert linked_list.first().value == 1
    assert linked_list.last().value == 9

    linked_list.remove(1)
    prepared_list.remove(1)
    linked_list.remove(5)
    prepared_list.remove(5)

    assert linked_list.all() == prepared_list

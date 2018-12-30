from data_structures.linked_list import LinkedList


def test_double_linked_list():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(28)
    linked_list.append(48)

    assert linked_list.size == 5
    assert repr(linked_list) == '[1 2 3 28 48]'

    linked_list.prepend(0)

    assert repr(linked_list) == '[0 1 2 3 28 48]'

    linked_list.remove(3)
    assert repr(linked_list) == '[0 1 2 28 48]'

    linked_list.remove(0)

    assert repr(linked_list) == '[1 2 28 48]'
    assert linked_list.size == 4

    assert repr(linked_list.find(2)) == '2'

    linked_list.reverse()
    assert repr(linked_list) == '[48 28 2 1]'

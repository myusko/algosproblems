from data_structures.linked_list import LinkedList


EXPECTED_STRING_REPRESENTATION = 'Node(1) -> Node(2) | Node(2) -> Node(3) | ' \
                                 'Node(3) -> Node(28) |' \
                                 ' Node(28) -> Node(48) |' \
                                 ' Node(48) -> Node(empty)'


def test_single_linked_list():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(28)
    linked_list.append(48)

    assert linked_list.size == 5
    assert linked_list.head.next.value == 1
    assert linked_list.head.next.next.value == 2
    assert linked_list.head.next.next.next.value == 3
    assert linked_list.head.next.next.next.next.value == 28
    assert linked_list.head.next.next.next.next.next.value == 48
    assert linked_list.display() == EXPECTED_STRING_REPRESENTATION

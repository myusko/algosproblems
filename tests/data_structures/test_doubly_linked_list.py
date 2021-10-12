import pytest

from data_structures.linked_list import MyLinkedList


@pytest.fixture(scope="function")
def linked_list():
    return MyLinkedList()


def test_add_at_head(linked_list):
    linked_list.addAtHead(1)

    assert linked_list.get(0) == 1


def test_add_at_tail(linked_list):
    linked_list.addAtHead(1)
    linked_list.addAtTail(2)

    assert linked_list.get(1) == 2


def test_get(linked_list):
    linked_list.addAtHead(0)

    assert linked_list.get(0) == 0


def test_add_at_index(linked_list):
    linked_list.addAtHead(0)
    linked_list.addAtHead(1)
    linked_list.addAtIndex(1, 3)

    assert linked_list.get(1) == 3


def test_delete_at_index(linked_list):
    linked_list.addAtHead(0)
    linked_list.addAtHead(1)
    linked_list.addAtIndex(1, 3)

    assert linked_list.get(1) == 3

    linked_list.deleteAtIndex(1)

    assert linked_list.get(1) == 0


def test_repr(linked_list):
    linked_list.addAtHead(0)
    linked_list.addAtHead(1)
    linked_list.addAtTail(3)

    assert repr(linked_list) == "1->0->3"

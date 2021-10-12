class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:
    def __init__(self):
        # Dummy objects to handle IndexError
        self._head = Node(None)
        self._tail = Node(None)

        self._head.next = self._tail
        self._tail.prev = self._head

    def get(self, index: int) -> int:
        """Get a node by index"""
        current_node = self._head.next

        while index != 0 and current_node:
            current_node = current_node.next
            index -= 1

        if (
            current_node is None
            or current_node is self._tail
            or current_node is self._head
        ):
            return -1

        return current_node.val

    def addAtHead(self, val: int) -> None:
        """Add a node to at head"""
        new_node = Node(val)

        next_node = self._head.next

        new_node.next = next_node
        next_node.prev = new_node

        self._head.next = new_node
        new_node.prev = self._head

    def addAtTail(self, val: int) -> None:
        """Add a node to at tail"""
        new_node = Node(val)

        prev = self._tail.prev

        prev.next = new_node
        new_node.prev = prev
        new_node.next = self._tail
        self._tail.prev = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        """Add a node before the specific value"""
        new_node = Node(val)

        current_node = self._head.next

        while index != 0 and current_node:
            current_node = current_node.next
            index -= 1

        prev = current_node.prev
        prev.next = new_node
        new_node.prev = prev
        new_node.next = current_node
        current_node.prev = new_node

    def deleteAtIndex(self, index: int) -> None:
        """Delete a node by specific index"""
        current_node = self._head.next

        while index != 0 and current_node:
            current_node = current_node.next
            index -= 1

        if (
            current_node is None
            or current_node is self._head
            or current_node is self._tail
        ):
            return

        prev = current_node.prev
        next = current_node.next

        prev.next = next
        next.prev = prev

    def __repr__(self):
        """Represent the DoublyLinkedList as string"""
        current_node = self._head.next
        result = []

        while current_node.next:
            result.append(current_node.val)
            current_node = current_node.next

        return "->".join(list(map(str, result)))

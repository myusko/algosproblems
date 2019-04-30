class Node:
    def __init__(self, val, prev, next_):
        self.value = val
        self.prev = prev
        self.next = next_

    def __repr__(self):
        return repr(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Add a value to a LinkedList"""
        if not isinstance(value, int):
            raise ValueError('Value must be of integer type')

        if self.head is None:
            self.head = Node(value, None, None)
            return

        last = self.__get_last()
        last.next = Node(value, last, None)

    def all(self):
        """Returns a list of nodes values"""
        result = []
        current = self.head

        while current:
            result.append(current.value)
            current = current.next

        return result

    def size(self):
        """Returns a LinkedList size"""
        return len(self.all())

    def first(self):
        """Returns a first node of a LinkedList"""
        return self.head

    def last(self):
        """Returns a last node of a LinkedList"""
        return self.__get_last()

    def maximum(self):
        """Returns a minimum integer of a LinkedList"""
        return max(self.all())

    def minimum(self):
        """Returns a maximum integer of a LinkedList"""
        return min(self.all())

    def remove(self, value):
        """Removes a node from a LinkedList"""
        current = self.head

        while current:
            if current.value == value:
                if current is self.head:
                    self.head = current.next
                    return

                prev = current.prev
                next_ = current.next
                next_.prev = current.prev

                prev.next = next_

            current = current.next

    def reverse(self):
        """Reverse a LinkedList"""
        last = self.__get_last()
        result = []

        while last:
            result.append(last.value)
            last = last.prev
        return result

    def __get_last(self):
        """Returns a last node of a LinkedList"""
        last = self.head

        while last:
            if last.next is None:
                return last
            last = last.next

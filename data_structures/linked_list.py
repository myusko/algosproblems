class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return f'Node({self.value}) -> Node({self.next.value if self.next else "empty"})'


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, value):
        new_node = Node(value)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    @property
    def size(self):
        size = 0
        current = self.head

        while current.next is not None:
            size += 1
            current = current.next
        return size

    def display(self):
        current = self.head
        result = []
        while current.next is not None:
            result.append(str(current.next))
            current = current.next
        return ' | '.join(result)



linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(28)
linked_list.append(48)
print(linked_list.display())
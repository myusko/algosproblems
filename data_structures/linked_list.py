class Node:
    def __init__(self, value=None, previous=None, next_=None):
        self.value = value
        self.previous = previous
        self.next = next_

    def __repr__(self):
        return repr(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        new_head = Node(value=value, next_=self.head)
        if self.head:
            self.head.previous = self.head
        self.head = new_head

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return

        current = self.head

        while current.next:
            current = current.next
        current.next = Node(value, previous=current)

    def find(self, value):
        current = self.head

        while current and current.value != value:
            current = current.next
        return current

    def remove_element(self, node):
        if node.previous:
            node.previous.next = node.next
        if node.next:
            node.next.previous = node.previous
        if node is self.head:
            self.head = node.next
        node.previous = None
        node.next = None

    def remove(self, value):
        node = self.find(value)
        self.remove_element(node)
        return True

    def reverse(self):
        current = self.head
        previous_node = None

        while current:
            previous_node = current.previous
            current.previous = current.next
            current.next = previous_node
            current = current.previous
        self.head = previous_node.previous

    @property
    def size(self):
        nodes = []
        current = self.head

        while current:
            nodes.append(current)
            current = current.next
        return len(nodes)

    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            nodes.append(repr(current))
            current = current.next
        return '[' + ' '.join(nodes) + ']'

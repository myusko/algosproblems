# Simple implementation of the HashSet
# https://en.wikipedia.org/wiki/Set_(abstract_data_type)

# Initial size of the MyHashSet is 15000
# If the size will be exceeded, we should create a new one
# with bigger space, and copy the existing one to the new one.
class MyHashSet:
    def __init__(self):
        self._length = 15000
        self._buckets = [[] for _ in range(self._length)]

    def hash(self, key: int) -> int:
        return key % self._length

    def add(self, key: int) -> None:
        index = self.hash(key)
        if key not in self._buckets[index]:
            self._buckets[index].append(key)

    def remove(self, key: int) -> None:
        index = self.hash(key)
        if key in self._buckets[index]:
            self._buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        if key in self._buckets[index]:
            return True
        return False

from data_structures.hash_set import MyHashSet


class TestMyHashSet:
    hash_set = MyHashSet()

    def test_add_value(self):
        self.hash_set.add(5)

        assert self.hash_set.contains(5)

    def test_remove_vale(self):
        self.hash_set.add(10)

        assert self.hash_set.contains(10)

        self.hash_set.remove(10)

        assert not self.hash_set.contains(10)

class HashTable:
    """
    Attributes:
        size
        _slots
        _data
    Methods:
        put(root, data)
        get(root)
        hash_function(root, _size)
        rehash(old_hash, _size)
    """
    def __init__(self, size):
        self._size = size
        self._slots = [None] * self._size
        self._data = [None] * self._size

    def __len__(self):
        return self._size

    def __contains__(self, key):
        key = self.hash_function(key, len(self._slots))
        return self._slots[key] is not None

    def __setitem__(self, key, data):
        self.put(key, data)

    def __getitem__(self, key):
        return self.get(key)

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self._slots))
        if self._slots[hash_value] is None:
            self._slots[hash_value] = key
            self._data[hash_value] = data
        else:
            if self._slots[hash_value] == key:
                self._data[hash_value] == data       # replace
            else:
                next_slot = self.rehash(hash_value, len(self._slots))
                while self._slots[next_slot] is not None and self._slots[next_slot] is not key:
                    next_slot = self.rehash(next_slot, len(self._slots))
                if self._slots[next_slot] is None:
                    self._slots[next_slot] = key
                    self._data[next_slot] = data
                else:
                    self._data[next_slot] = data     # replace

    def get(self, key):
        start_slot = self.hash_function(key, len(self._slots))
        data = None
        stop = False
        found = False
        position = start_slot
        while self._slots[position] is not None and not found and not stop:
            if self._slots[position] == key:
                found = True
                data = self._data[position]
            else:
                position = self.rehash(position, len(self._slots))
                if position == start_slot:
                    stop = True
        return data

    def get_slots(self):
        return self._slots

    def get_data(self):
        return self._data

    @staticmethod
    def hash_function(key, size):
        return key % size

    @staticmethod
    def rehash(old_hash, size):
        return (old_hash+1) % size


if __name__ == "__main__":
    table = HashTable(11)
    table[54] = "cat"
    table[26] = "dog"
    table[93] = "lion"
    table[17] = "tiger"
    table[77] = "bird"
    table[31] = "cow"
    table[44] = "goat"
    table[55] = "pig"
    table[20] = "chicken"
    table[10] = "duck"
    print(table.get_slots())
    print(table.get_data())
    print(19 in table)

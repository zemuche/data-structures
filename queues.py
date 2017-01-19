from structures.linked_lists import UnorderedList


class Queue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._items = [None] * Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, item):
        if self._size == len(self._items):
            self._resize(2 * len(self._items))
        avail = (self._front + self._size) % len(self._items)
        self._items[avail] = item
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        item = self._items[self._front]
        self._items[self._front] = None
        self._front = (self._front + 1) % len(self._items)
        self._size -= 1
        if 0 < self._size < len(self._items)//4:
            self._resize(len(self._items)//2)
        return item

    def _resize(self, cap):
        old = self._items
        self._items = [None] * cap
        walk = self._front
        for i in range(self._size):
            self._items[i] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def first(self):
        return self._items[self._front]

    def print_queue(self):
        while not self.is_empty():
            print(self.dequeue())


class LinkedQueue:
    def __init__(self):
        self.items = UnorderedList()

    def __repr__(self):
        return repr(self.items)

    def __len__(self):
        return len(self.items)

    def isempty(self):
        """Return True is queue is empty."""
        return len(self.items) == 0

    def enqueue(self, item):
        """Add item to the back of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the first element of the queue."""
        if self.isempty():
            raise ValueError("dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        """Return the first item in the queue without removing it."""
        if self.isempty():
            raise ValueError("peek from empty queue")
        return self.items.__index(0)


class CircularQueue:
    def __init__(self):
        self._length = 0
        self._tail = None

    def __repr__(self):
        current = self._tail.next
        output = "["
        if self._length > 0:
            output += str(current)
            for i in range(self._length - 1):
                current = current.next
                output += ", " + str(current)
        return output + "]"

    def __len__(self):
        return self._length

    def is_empty(self):
        return self._length == 0

    def enqueue(self, item):
        """Add item to the back of the queue."""
        new_item = Node(item)
        if self.is_empty():
            new_item.next = new_item
        else:
            new_item.next = self._tail.next
            self._tail.next = new_item
        self._tail = new_item
        self._length += 1

    def dequeue(self):
        """Remove and return the first element of the queue."""
        if self.is_empty():
            return "Queue is empty"
        old_head = self._tail.next
        if self._length == 1:
            self._tail = None
        else:
            self._tail.next = old_head.next
        self._length -= 1
        return old_head

    def rotate(self):
        """Rotate front item to the back of the queue."""
        if self._length > 0:
            self._tail = self._tail.next

    def peek(self):
        if self.is_empty():
            return "List is empty"
        return self._tail.next


class PriorityQueue:
    def __init__(self):
        self.items = []

    def __repr__(self):
        output = ""
        for i in self.items:
            output += str(i) + "\n"
        return output

    def isempty(self):
        return self.items == []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        self.items[maxi:maxi+1] = []
        return item


class Golfer:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return "{0}{1}".format(str(self.name).ljust(20, '.'), self.score)

    def __lt__(self, other):
        if self.score < other.score:
            return True
        elif self.score > other.score:
            return False
        else:
            if self.name > other.name:
                return True
            elif self.name < other.name:
                return False
            return 0


def main():
    # Priority Queue example
    # tiger = Golfer("Tiger Woods", 61)
    # zemene = Golfer("Zemene Muche", 61)
    # phil = Golfer("Phil Mickelson", 72)
    # hal = Golfer("Hal Sutton", 69)
    # pq = PriorityQueue()
    # pq.insert(tiger)
    # pq.insert(phil)
    # pq.insert(hal)
    # pq.insert(zemene)
    # print(pq)

    # Circular Queue example
    cq = CircularQueue()
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    print(cq)
    cq.rotate()
    print(cq)
    print(cq.dequeue())
    print(cq.dequeue())
    print(cq.dequeue())
    print(cq.dequeue())


if __name__ == "__main__":
    main()

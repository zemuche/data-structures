import sys


class Node:
    def __init__(self, item=None, position=0):
        self._item = item
        self._next = None
        self._position = position

    def __repr__(self):
        return str(self.item)

    @property
    def item(self):
        return self._item

    @property
    def next(self):
        return self._next

    @item.setter
    def item(self, item):
        self._item = item

    @next.setter
    def next(self, node):
        self._next = node

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, pos):
        self._position = pos


class LinkedList:
    """
    Attributes:
        length
        head node
        tail node
    Methods:
        isempty(): returns True if linked list is empty; False otherwise.
        add(item): adds item to front of list, shifting everything to the end.
        append(item): adds item to the end of the linked list.
        insert(pos, item): inserts item to a given index of the linked list.
        remove(item): removes given item from the linked list.
        pop(): removes the last item of the linked list.
        pop(i): removes item at index i; negative indices work.
        index(item): returns the item at the given index.
        find(item): returns the index of the give item.
    """

    def __init__(self, *args):
        self.mem_size = 0
        self.length = 0
        self.head = None
        self.tail = None
        self.extend(iter(args))

    def __repr__(self):
        return '[' + ', '.join(str(n) for n in iter(self)) + ']'

    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __reversed__(self):
        self._reverse(self.head)
        return ulist(iter(self))

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.__getslice(index.start, index.stop, index.step)
        else:
            return self.__index(index)

    def __add__(self, other):
        try:
            self.extend(ulist(other))
        except TypeError:
            raise TypeError("other must be a sequence")
        return self

    def __mul__(self, num):
        try:
            for _ in range(int(num) - 1):
                self.extend(list(self))
        except ValueError:
            raise ValueError("num must be an int")
        return self

    def __sizeof__(self):
        return self.mem_size

    def extend(self, other):
        if isinstance(self, UnorderedList):
            for item in other:
                self.append(item)
        elif isinstance(self, OrderedList):
            for item in other:
                self.add(item)

    def isempty(self):
        """Return True if linked list is empty; False otherwise."""
        return self.head is None

    def __getslice(self, start, stop, step):
        res = UnorderedList()
        start = 0 if start is None else start
        stop = len(self) if stop is None else stop
        stop = stop + len(self) if stop < 0 else stop
        step = 1 if step is None else step
        if step <= 0:
            if step == 0:
                raise ValueError("slice step cannot be zero")
            stop = -1 if stop == len(self) else stop
            start = len(self) - 1 if start == 0 else start
        for i in range(start, stop, step):
            res.append(self.__index(i))
        return res

    def __index(self, index):
        """Return the item at the given index."""
        if len(self) - 1 < index or index < -len(self):
            raise ValueError("list index out of range")
        if index < 0:
            index += self.length
        for i, item in enumerate(self):
            if i == index:
                return item
        return None

    def find(self, item):
        """Return the index of the given item."""
        for i, a in enumerate(self):
            if a == item:
                return i
        return -1

    def count(self, item):
        cnt = 0
        current = self.head
        while current is not None:
            if current.item == item:
                cnt += 1
            current = current.next
        return cnt

    def remove(self, item):
        """Remove given item from the linked list."""
        current = self.head
        previous = None
        found = False
        if current is None:
            return "Empty list"
        while current is not None and not found:
            if current.item == item:
                found = True
            else:
                previous = current
                current = current.next
        if previous is None:
            self.head = current.next
        elif found:
            previous.next = current.next
        else:
            return str(item) + " not in list"
        self.length -= 1
        self._index_correct(self.head)
        return str(item) + " removed"

    def popleft(self):
        popped = self.head
        self.head = popped.next
        self.length -= 1
        return popped

    def pop(self, position=None):
        """pop(): remove the last item of the linked list.
           pop(i): remove item at index i; negative indices work."""
        if self.isempty():
            raise IndexError("pop from empty stack")
        if position is None:
            position = self.length - 1
        current = self.head
        previous = None
        popped = None
        found = False
        if position >= self.length:
            raise IndexError("pop from empty stack")
        elif position < 0:
            position += self.length
        while not found:
            if current.position == position:
                popped = current
                found = True
            else:
                previous = current
                current = current.next
        if previous is None:
            self.head = current.next
        else:
            previous.setnext(current.next)
            if previous.next is None:
                self.tail = previous
        self.length -= 1
        self._index_correct(self.head)
        return popped.item

    def addwith(self, other):
        """Add respective elements of other to instance if equal length."""
        if len(other) != len(self):
            raise TypeError("addition of unequal lists")
        cur1 = self.head
        try:
            other = ulist(other)
        except TypeError:
            raise TypeError("can't perform operation.")
        else:
            cur2 = other.head
            while cur1 is not None:
                cur1.item += cur2.item
                cur1, cur2 = cur1.next, cur2.next

    def subwith(self, other):
        """Subtract respective elements of other from instance if equal length."""
        cur1 = self.head
        if isinstance(other, LinkedList) and len(self) == len(other):
            cur2 = other.head
            while cur1 is not None:
                cur1.item -= cur2.item
                cur1, cur2 = cur1.next, cur2.next
        else:
            raise TypeError("Can't perform operation.")

    def addtoeach(self, num):
        """Add num to each element of instance."""
        if not (isinstance(num, int) or isinstance(num, float)):
            raise TypeError("num must be int or float: you provided "
                            + str(type(num)))
        cur = self.head
        while cur is not None:
            cur.item += num
            cur = cur.next

    def subfromeach(self, num):
        """Add num to each element of instance."""
        if not (isinstance(num, int) or isinstance(num, float)):
            raise TypeError("num must be int or float: you provided "
                            + str(type(num)))
        cur = self.head
        while cur is not None:
            cur.item -= num
            cur = cur.next

    def multeach(self, num):
        """Add num to each element of instance."""
        if not (isinstance(num, int) or isinstance(num, float)):
            raise TypeError("num must be int or float: you provided "
                            + str(type(num)))
        cur = self.head
        while cur is not None:
            cur.item *= num
            cur = cur.next

    def diveach(self, num):
        """Add num to each element of instance."""
        if not (isinstance(num, int) or isinstance(num, float)):
            raise TypeError("num must be int or float: you provided "
                            + str(type(num)))
        elif num == 0:
            raise ZeroDivisionError()
        cur = self.head
        while cur is not None:
            cur.item /= num
            cur = cur.next

    def intdiveach(self, num):
        """Add num to each element of instance."""
        if not (isinstance(num, int) or isinstance(num, float)):
            raise TypeError("num must be int or float: you provided "
                            + str(type(num)))
        elif num == 0:
            raise ZeroDivisionError()
        cur = self.head
        while cur is not None:
            cur.item //= num
            cur = cur.next

    def modeach(self, num):
        """Add num to each element of instance."""
        cur = self.head
        while cur is not None:
            cur.item %= num
            cur = cur.next

    def _reverse(self, head):
        self.head = self.reverse_list(head)

    @classmethod
    def fromiter(cls, iterable):
        return cls(*iterable)

    @staticmethod
    def reverse_list(head):
        new_head = None
        while head:
            head.next, head, new_head = new_head, head.next, head
        return new_head

    @staticmethod
    def _index_correct(node):
        position = 0
        while node is not None:
            node.position = position
            node = node.next
            position += 1


class CircularList:
    def __init__(self, *args):
        self._length = 0
        self._tail = None
        self.extend(iter(args))

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

    def __iter__(self):
        if self._length > 0:
            current = self._tail.next
            for i in range(self._length):
                yield current.item
                current = current.next

    def isempty(self):
        return self._length == 0

    def append(self, item):
        new_item = Node(item)
        if self.isempty():
            new_item.next = new_item
        else:
            new_item.next = self._tail.next
            self._tail.next = new_item
        self._tail = new_item
        self._length += 1

    def extend(self, other):
        for item in other:
            self.append(item)

    def pop(self):
        """Remove and return the first element of the queue."""
        if self.isempty():
            return "Queue is empty"
        old_head = self._tail.next
        if self._length == 1:
            self._tail = None
        else:
            self._tail.next = old_head.next
        self._length -= 1
        return old_head

    @classmethod
    def fromiter(cls, iterable):
        return cls(*iterable)


class DoublyList:
    class _Node:
        def __init__(self, item, prev, next, position=0):
            self._item = item
            self._prev = prev
            self._next = next
            self._position = position

        def __repr__(self):
            return str(self._item)

        @property
        def item(self):
            return self._item

        @item.setter
        def item(self, item):
            self._item = item

        @property
        def next(self):
            return self._next

        @next.setter
        def next(self, item):
            self._next = item

        @property
        def prev(self):
            return self._prev

        @prev.setter
        def prev(self, item):
            self._prev = item

        @property
        def position(self):
            return self._position

        @position.setter
        def position(self, pos):
            self._position = pos

    def __init__(self, *args):
        self._header = self._Node(None, None, None, None)
        self._trailer = self._Node(None, None, None, None)
        self._header.next = self._trailer
        self._trailer.prev = self._header
        self._length = 0
        self.extend(iter(args))

    def __repr__(self):
        current = self._header.next
        output = "["
        if self._length > 0:
            output += str(current)
            for i in range(self._length - 1):
                current = current.next
                output += ", " + str(current)
        return output + "]"

    def __len__(self):
        return self._length

    def __iter__(self):
        if self._length > 0:
            current = self._header.next
            for i in range(self._length):
                yield current.item
                current = current.next

    def isempty(self):
        return self._length == 0

    def peek_left(self):
        if self.isempty():
            raise ValueError("peek from empty list")
        return self._header.next.item

    def peek_right(self):
        if self.isempty():
            raise ValueError("peek from empty list")
        return self._trailer.prev.item

    def append(self, item):
        self._insert_between(item, self._trailer.prev, self._trailer)

    def prepend(self, item):
        self._insert_between(item, self._header, self._header.next)

    def popleft(self):
        if self.isempty():
            raise ValueError("pop from empty list")
        return self._delete_node(self._header.next)

    def popright(self):
        if self.isempty():
            raise ValueError("pop from empty list")
        return self._delete_node(self._trailer.prev)

    def extend(self, other):
        for item in other:
            self.append(item)

    def _insert_between(self, item, predecessor, successor):
        new_item = self._Node(item, predecessor, successor)
        predecessor.next = new_item
        successor.prev = new_item
        self._length += 1
        self._index_correct(self._header.next)
        return new_item

    def _delete_node(self, node):
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self._length -= 1
        self._index_correct(self._header.next)
        return node

    @classmethod
    def fromiter(cls, iterable):
        return cls(*iterable)

    @staticmethod
    def _index_correct(value):
        position = 0
        while value is not None:
            value.position = position
            position += 1
            value = value.next


class UnorderedList(LinkedList):
    def __init__(self, *args):
        LinkedList.__init__(self, *args)

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            self._setslice(index.start, index.stop, value)
        else:
            index = index + len(self) if index < 0 else index
            current = self.head
            while current is not None:
                if current.position == index:
                    current.item = value
                current = current.next

    def add(self, item):
        """Add item to the beginning of linked list."""
        new_item = Node(item)
        new_item.next = self.head
        self.head = new_item
        self.length += 1
        self._index_correct(self.head)
        if self.length == 1:
            self.tail = self.head
        self.mem_size += sys.getsizeof(item)

    def append(self, item):
        """Add item to the end of the linked list."""
        new_item = Node(item)
        new_item.next = None
        if self.head is None:
            self.head = self.tail = new_item
        else:
            self.tail.next = new_item
            self.tail = new_item
        self.length += 1
        self._index_correct(self.head)
        self.mem_size += sys.getsizeof(new_item)

    def insert(self, pos, item):
        """Insert item to a given index of the linked list."""
        if pos == 0:
            self.add(item)
        elif pos == len(self):
            self.append(item)
        elif pos > len(self):
            raise IndexError("index out of range")
        else:
            node = Node(item, pos)
            current = self.head
            previous = None
            while current.position != pos:
                previous = current
                current = current.next
            previous.next = node
            node.next = current
        self.length += 1
        self._index_correct(self.head)
        self.mem_size += sys.getsizeof(item)

    def _setslice(self, i, j, sequence):
        i = 0 if i is None else i
        i = i + len(self) if i < 0 else i
        j = len(self) if j is None else j
        j = j + len(self) if j < 0 else j
        indices = list(range(i, j))
        count = 0
        current_index = 0
        for index in indices:
            self[index] = sequence[count]
            current_index = index
            count += 1
        current_index += 1
        while count < len(sequence):
            self.insert(current_index, sequence[count])
            current_index += 1
            count += 1


class OrderedList(LinkedList):
    def add(self, item):
        """Add item to linked list while keeping the order."""
        node = Node(item)
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.item > item:
                stop = True
            else:
                previous = current
                current = current.next
        if previous is None:
            node.next = self.head
            self.head = node
        else:
            node.next = current
            previous.next = node
        self.length += 1
        self._index_correct(self.head)


def ulist(other):
    return UnorderedList().fromiter(iter(other))


def olist(other):
    return OrderedList().fromiter(iter(other))


def clist(other):
    return CircularList().fromiter(iter(other))


def dlist(other):
    return DoublyList.fromiter(iter(other))


def main():
    n = 10

    list0 = []
    for i in range(n):
        list0.append(i)
    print(list0)

    list1 = UnorderedList()
    for i in range(n):
        list1.append(i)
    print(list1)

    revlist0 = list0[::-1]
    revlist1 = list1[::-1]
    print(revlist0, revlist1)

    list0[5:7] = [11, 12, 13, 14, 15]
    list1[5:7] = [11, 12, 13, 14, 15]
    print(list0)
    print(list1)

    # print(sys.getsizeof(list0), sys.getsizeof(list1))
    # for a, b in zip(list0, list1):
    #     print(sys.getsizeof(a), sys.getsizeof(b))


if __name__ == "__main__":
    main()

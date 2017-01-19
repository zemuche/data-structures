from collections import deque
from structures.linked_lists import DoublyList


class Deque:
    def __init__(self):
        self.items = deque()

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        return self.items == 0

    def add_front(self, item):
        self.items.appendleft(item)

    def pop_rear(self):
        return self.items.popleft()

    def add_rear(self, item):
        self.items.append(item)

    def pop_front(self):
        return self.items.pop()

    def first(self):
        return self.items[0]

    def last(self):
        return self.items[-1]


class LinkedDeque:
    def __init__(self, *args):
        self.items = DoublyList(*args)

    def __repr__(self):
        return repr(self.items)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def add_front(self, item):
        self.items.prepend(item)

    def add_rear(self, item):
        self.items.append(item)

    def pop_front(self):
        return self.items.popleft()

    def pop_rear(self):
        return self.items.popright()

    def front(self):
        return self.items.peek_left()

    def rear(self):
        return self.items.peek_right()


class PositionList(DoublyList):
    """A Sequential container of elements allowing positional access."""

    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        @property
        def container(self):
            return self._container

        @container.setter
        def container(self, p):
            self._container = p

        @property
        def node(self):
            return self._node

        @node.setter
        def node(self, e):
            self._node = e

        def element(self):
            return self.node.item

        def __eq__(self, other):
            if type(other) is type(self) and other.node is self.node:
                return True
            return False

    def _validate(self, p):
        """Return position's node, or raise error"""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p.container is not self:
            raise ValueError("p does not belong to this container")
        if p.node.next is None:
            raise ValueError("p is not longer valid")
        return p.node

    def _make_position(self, node):
        """Return Position instance for given code (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None
        return self.Position(self, node)

    def first(self):
        return self._make_position(self._header.next)

    def last(self):
        return self._make_position(self._trailer.prev)

    def before(self, p):
        """Return the Position just before Position p"""
        node = self._validate(p)
        return self._make_position(node.prev)

    def after(self, p):
        """Return the Position just after Position p"""
        node = self._validate(p)
        return self._make_position(node.next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        """Add element between existing ndoes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header.next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer.prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Postion."""
        original = self._validate(p)
        return self._insert_between(e, original.prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original.next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        """Replace element at Position p with e, return former element at p."""
        original = self._validate(p)
        old_value = original.item
        original.item = e
        return old_value

    def sort(self):
        """Sort PositionalList of comparable elements in increasing order."""
        if len(self) > 1:                       # otherwise no need to sort
            marker = self.first()
            while marker != self.last():
                pivot = self.after(marker)      # next item to place
                value = pivot.element()
                if value > marker.element():    # pivot is already sorted
                    marker = pivot              # pivot becomes new marker
                else:                           # must relocate pivot
                    walk = marker               # find leftmost item > value
                    while walk != self.first() and self.before(walk).element() > value:
                        walk = self.before(walk)
                    self.delete(pivot)
                    self.add_before(walk, value)   # reinsert value before walk
        return self


if __name__ == "__main__":
    # d = LinkedDeque()
    # d.add_front(1)
    # d.add_rear("World")
    # d.add_front(2)
    # d.add_rear("Hello")
    # d.add_front(3)
    # d.add_rear("Zemene")
    # print(len(d))
    # print(sorted(d))

    pl = PositionList()
    pl.add_first(5)
    pl.add_first(10)
    pl.add_first(20)
    pl.add_last(7)
    pl.add_first(45)
    print(pl)
    print(pl.sort())

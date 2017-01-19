from structures.linked_lists import UnorderedList


class Stack:
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def isempty(self):
        return self._items == []

    def push(self, item):
        self._items.append(item)

    def pop(self, item=None):
        if item == 0:
            return self._items.pop(0)
        return self._items.pop()

    def top(self):
        return self._items[len(self._items) - 1]


class LinkedStack:
    def __init__(self):
        self.items = UnorderedList()

    def __repr__(self):
        return repr(self.items)

    def __len__(self):
        return len(self.items)

    def isempty(self):
        """Return True is stack is empty."""
        return self.items.isempty()

    def push(self, item):
        """Add item to the top of the stack."""
        self.items.add(item)

    def pop(self):
        """Remove and return the top element of the stack."""
        if self.isempty():
            raise ValueError("pop from empty stack")
        return self.items.pop(0)

    def peek(self):
        """Return the top item on the stack without removing it."""
        if self.isempty():
            raise ValueError("peek from empty stack")
        return self.items.__index(0)


def main():
    # Linked Stack Example
    ls = LinkedStack()
    ls.push(5)
    ls.push(10)
    ls.push(30)
    ls.push(20)
    print(ls)
    print("\nLength:", len(ls))
    print(ls.peek())


if __name__ == '__main__':
    main()

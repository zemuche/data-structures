class BinaryHeap:
    """
    BinaryHeap() creates a new, empty, binary heap.
    insert(k) adds a new item to the heap.
    find_min() returns item with the min key value, leaving item in the heap.
    del_min() returns item with the min key value, removing item from the heap.
    is_empty() returns true if the heap is empty, false otherwise.
    size() returns the number of items in the heap.
    build_heap(list) builds a new heap from a list of keys.
    """

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def __repr__(self):
        return str(self.heap_list)

    def is_empty(self):
        return self.current_size == 0

    def insert(self, new_item):
        self.heap_list.append(new_item)
        self.current_size += 1
        self.percolate_up(self.current_size)

    def del_min(self):
        retrieve_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.percolate_down(1)
        return retrieve_value

    def build_heap(self, alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        while i > 0:
            self.percolate_down(i)
            i -= 1

    def size(self):
        return self.current_size

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                temp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = temp
            i //= 2

    def percolate_down(self, i):
        while i*2 <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = temp
            i = mc

    def min_child(self, i):
        if i*2 + 1 > self.current_size:
            return i*2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i*2
            else:
                return i*2 + 1


def main():
    my_list = [5, 10, 1, 20, 0]
    bh = BinaryHeap()
    bh.build_heap(my_list)
    print(bh)


if __name__ == '__main__':
    main()

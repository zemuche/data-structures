import ctypes
from time import time


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0                 # Count actual elements
        self._capacity = 1          # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array

    def __str__(self):
        return str(self._A)

    def __len__(self):
        """Return the number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError("Invalid index")
        return self._A[k]                       # retrieve from array

    def append(self, obj):
        """Add object to end of the array"""
        if self._n == self._capacity:           # not enough room
            self._resize(2 * self._capacity)    # double capacity
        self._A[self._n] = obj
        self._n += 1

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # for simplicity, we assume 0 <= k <= n in this version
        if self._n == self._capacity:           # not enough room
            self._resize(2 * self._capacity)    # so double capacity
        for j in range(self._n, k, -1):         # shift rightmost first
            self._A[j] = self._A[j-1]
        self._A[k] = value                      # store newest element
        self._n += 1

    def remove(self, value):
        """Remove first occurrence of value (or rise ValueError)."""
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:             # found a match
                for j in range(k, self._n-1):   # shift others to fill gp
                    self._A[j] == self._A[j+1]
                self._A[self._n - 1] = None     # help garbage collection
                self._n -= 1                    # we all one less item
                return                          # exit immediately
        raise ValueError("Value not found")

    def _resize(self, c):                       # nonpublic utility
        """Resize internal array to capacity c."""
        B = self._make_array(c)                 # new(larger) array
        for k in range(self._n):                # for each in A
            B[k] = self._A[k]
        self._A = B                             # use larger array
        self._capacity = c

    @staticmethod
    def _make_array(c):
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()


def compute_average(n):
    data = []
    start = time()
    for k in range(n):
        data.insert(n, None)
    end = time()
    return (end - start) / n


if __name__ == "__main__":
    print("Dynamic array")
    da = DynamicArray()
    da.append(5)
    da.append(10)
    da.append(15)
    da.append(20)
    print(list(da))
    da.remove(15)
    print(list(da))
    # print(compute_average(10000))


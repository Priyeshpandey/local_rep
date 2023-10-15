import heapq
from copy import deepcopy


class Heap:
    def __init__(self, arr):
        self.heap = arr
        self.heapify()

    def top(self) -> int:
        return self.heap[0]

    def pop(self) -> int:
        # replace top with last
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self._heapify(0, len(self.heap) - 1)
        return self.heap.pop()


    def insert(self, key: int) -> None:
        self.heap.append(key)
        n = len(self.heap)
        self._heapify(n // 2 - 1, n)

    def heapify(self) -> None:  # key is index
        n = len(self.heap)

        for pos in range(n // 2, -1, -1):
            self._heapify(pos, n)

    def find(self, key: int) -> bool:
        return self._find(key, 0)

    def traverse(self) -> None:
        print(self.heap)

    def _heapify(self, pos, n):
        if pos == n:
            return
        parent = pos
        leftChild = 2 * pos + 1
        rightChild = 2 * pos + 2

        if leftChild < n and self.heap[leftChild] < self.heap[pos]:
            # swap pos with leftChild
            pos, leftChild = leftChild, pos

        if rightChild < n and self.heap[rightChild] < self.heap[pos]:
            # swap pos with leftChild
            pos, rightChild = rightChild, pos

        if parent != pos:
            self.heap[parent], self.heap[pos] = self.heap[pos], self.heap[parent]
            self._heapify(pos, n)

    def _find(self, key, pos):
        if pos >= len(self.heap):
            return False
        if key == self.heap[pos]: return True

        return self._find(key, 2 * pos + 1) or self._find(key, 2 * pos + 2)


if __name__ == '__main__':
    arr = [5, 4, 6, 8, 2, 1]
    hp = Heap(arr)
    hp.traverse()
    print(hp.find(8), hp.find(9))
    hp.insert(3)
    hp.traverse()
    hp.insert(7)
    hp.traverse()
    print(hp.pop())
    hp.traverse()

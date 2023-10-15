# https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/
import heapq
from sys import maxsize


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.leftHeap = []
        self.rightHeap = []
        self.length = 0
        self.median = -10 ** 6

    def pushLeftHeap(self, num):
        if len(self.leftHeap) == 0:
            self.leftHeap.append(-num)
            heapq.heapify(self.leftHeap)  # Max heap
            return
        heapq.heappush(self.leftHeap, -num)

    def getLeftHeapTop(self):
        return -self.leftHeap[0]

    def popLeftHeap(self):
        return -heapq.heappop(self.leftHeap)

    def pushRightHeap(self, num):
        if len(self.rightHeap) == 0:
            self.rightHeap.append(num)
            heapq.heapify(self.rightHeap)  # Max heap
            return
        heapq.heappush(self.rightHeap, num)

    def getRightHeapTop(self):
        return self.rightHeap[0]

    def popRightHeap(self):
        return heapq.heappop(self.rightHeap)

    def addNum(self, num: int) -> None:  # O(log(max(|LeftHeap|,|RightHeap|))
        diff = len(self.leftHeap) - len(self.rightHeap)
        if num < self.median:
            if diff == -1:
                self.pushLeftHeap(num)
                self.median = (self.getLeftHeapTop() + self.getRightHeapTop()) / 2
            elif diff == 0:
                self.pushLeftHeap(num)
                self.median = self.getLeftHeapTop()
            else:
                leftTop = self.popLeftHeap()
                self.pushRightHeap(leftTop)
                self.pushLeftHeap(num)
                self.median = (self.getLeftHeapTop() + self.getRightHeapTop()) / 2
        else:
            if diff == 1:
                self.pushRightHeap(num)
                self.median = (self.getLeftHeapTop() + self.getRightHeapTop()) / 2
            elif diff == 0:
                self.pushRightHeap(num)
                self.median = self.getRightHeapTop()
            else:
                rightTop = self.popRightHeap()
                self.pushLeftHeap(rightTop)
                self.pushRightHeap(num)
                self.median = (self.getLeftHeapTop() + self.getRightHeapTop()) / 2

    def findMedian(self) -> float:  # O(1)
        return self.median


def check_assert(actual, expected):
    assert actual == expected, f'{actual} != {expected}'
    print('Success')


if __name__ == '__main__':
    mm = MedianFinder()
    mm.addNum(10)
    check_assert(mm.findMedian(), 10)
    mm.addNum(2)
    mm.addNum(7)
    check_assert(mm.findMedian(), 7)
    mm.addNum(20)
    check_assert(mm.findMedian(), 17 / 2)

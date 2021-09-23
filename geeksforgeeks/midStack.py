class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None


class Deque:
    def __init__(self, node: Node = None):
        self.mid = node
        self.top = node
        self.count = 0 if not node else 1

    def push_(self, x: int):
        self.count += 1
        if not self.top:
            self.top = Node(x)
            self.mid = self.top
            return
        self.top.next = Node(x)
        self.top.next.prev = self.top
        self.top = self.top.next
        if self.count % 2:
            self.mid = self.mid.next

    def pop(self) -> int:
        if not self.top:
            return -int('inf')
        self.count -= 1
        if self.count % 2 == 0:
            self.mid = self.mid.prev
        prev = self.top.prev
        topData = self.top.data
        del self.top
        self.top = prev
        return topData

    def getMid(self):
        if self.mid:
            return self.mid.data

        return -float('inf')

    def getTop(self) -> int:
        if self.top:
            return self.top.data

        return -int('inf')


if __name__=='__main__':
    arr = [1,2,3,4,5,6]
    stack = Deque()
    for i in arr:
        stack.push_(i)
        print(f'Top = {stack.getTop()}, Mid = {stack.getMid()}')
    print(stack.getTop(), stack.getMid())
    for i in arr:
        if i%2:
            stack.pop()
        else:
            stack.push_(i)
        print(f'Top = {stack.getTop()}, Mid = {stack.getMid()}')
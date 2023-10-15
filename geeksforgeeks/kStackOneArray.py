# https://www.geeksforgeeks.org/efficiently-implement-k-stacks-single-array/

class Stack:
    def __init__(self, k, N):
        self.size = N
        self.k = k
        self.arr = [0]*N
        self.top = [-1]*k
        self.next = [0]*N
        for i in range(1,N-1):
            self.next[i-1] = i
        self.next[N-1] = -1
        self.free = 0

    def push(self, sn, data):
        oldFree = self.free
        if oldFree == -1:
            raise Exception('Stack Overflow!!')
        self.free = self.next[oldFree] # newFreeSlot = nextOf(oldFree slot)
        self.next[oldFree] = self.top[sn] # next of oldFree = oldTop(sn)
        self.top[sn] = oldFree # newTop(sn) = oldFree slot
        self.arr[self.top[sn]] = data # update data at newTop(sn)

    def pop(self, sn):
        if self.top[sn] == -1:
            raise Exception('Stack Underflow!!')

        temp = self.free
        self.free = self.top[sn]    # current top becomes free
        self.top[sn] = self.next[self.top[sn]] # go to oldTop
        self.next[self.top[sn]] = temp # next free slot after sn top


if __name__=='__main__':
    stack = Stack(3, 10)
    arr = [1,20,2,3,6,9,8,4,60]
    for i, item in enumerate(arr):
        stack.push(i%3, item)
        print('Status : ', stack.arr)
        print('Top pos : ', [stack.top[x] for x in range(3)])

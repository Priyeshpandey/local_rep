class Stack:
    def __init__(self, arr):
        self.stack = []

    def push(self, e):
        self.stack.append(e)

    def pop(self):
        return self.stack.pop()

    def getTop(self):
        return self.stack[-1]


if __name__=='__main__':
    st = Stack([])
    st.push(10)
    st.push(20)
    print(st.getTop())
    print(st.pop())
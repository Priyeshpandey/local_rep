from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def buildTree(arr):
    q = deque()
    root = Node(arr[0])
    q.append(root)
    n = len(arr)
    i = 2
    while q:
        node = q.popleft()
        if i < n:
            node.left = Node(arr[i - 1])
            node.right = Node(arr[i])
            q.append(node.left)
            q.append(node.right)
        i += 2
    return root


def inorderIter(root):
    stack = []
    node = root

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.data, end='->')
            node = node.right

def preorderIter(root):
    stack = []
    node = root

    while stack or node:
        if node:
            print(node.data, end='->')
            stack.append(node.right)
            stack.append(node.left)
        node = stack.pop()

def postOrderIter(root):
    stack = []
    node = root

    while stack or node:
        if stack:
            node = stack.pop()

        if node:
            print(node.data)
            stack.append(node.right)
            stack.append(node.left)




if __name__=='__main__':
    #      1
    #   2     3
    # 4   5
    #1 2 4 5 3
    arr = [1,2,3,4,5]
    root = buildTree(arr)
    inorderIter(root)
    print('\n')
    preorderIter(root)
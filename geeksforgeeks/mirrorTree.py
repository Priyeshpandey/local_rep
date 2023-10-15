from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def mirror(root):
    if not root:
        return root

    left = mirror(root.left)
    right = mirror(root.right)

    root.left = right
    root.right = left

    return root


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end='->')
    inorder(root.right)


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
        i+=2
    return root


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    root = buildTree(arr)
    inorder(root)
    root = mirror(root)
    inorder(root)
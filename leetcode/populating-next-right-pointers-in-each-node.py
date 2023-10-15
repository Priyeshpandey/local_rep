from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = deque()
        q.append((root, 0))
        while q:
            node, lvl = q.popleft()
            left = node.left
            right = node.right
            if q and q[0][1] == lvl:
                node.next = q[0][0]
            if left:
                q.append((left, lvl + 1))
            if right:
                q.append((right, lvl + 1))
        return root


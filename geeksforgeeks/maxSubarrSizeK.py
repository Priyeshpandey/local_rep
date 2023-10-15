class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, node, key):
        if not node:
            return Node(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            return node

        node.height = 1 + max(self.height(node.left), self.height(node.right))

        balance = self.get_balance(node)

        # Left Left imbalance
        if balance > 1 and key < node.left.key:
            return self.rightRotate(node)

        # Right Right imbalance
        if balance < -1 and key > node.right.key:
            return self.leftRotate(node)

        # Left Right imbalance
        if balance > 1 and key > node.left.key:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        # Right left imbalance

        if balance < -1 and key < node.right.key:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def height(self, node) -> int:
        if not node:
            return 0

        return node.height

    def get_balance(self, node) -> int:
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rightRotate(self, y):
        x = y.left
        T2 = x.right if x else None

        # perform rotation
        if x:
            x.right = y
        y.left = T2

        # Update heights
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        if x:
            x.height = max(self.height(x.left), self.height(x.right)) + 1

        return x

    def leftRotate(self, y):
        x = y.right
        T2 = x.left if x else None

        # Left Rotate
        if x:
            x.left = y
        y.right = T2

        # Update Heights
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        if x:
            x.height = max(self.height(x.left), self.height(x.right)) + 1

        return x

    def delete(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self.delete(node.left, key)

        elif key > node.key:
            node.right = self.delete(node.right, key)

        else:
            # key found now delete this bastard
            # case 1: node with only one child or no child then simply delete current node
            # return child to current node's parent
            if not node.left or not node.right:
                temp = None
                if node.left:
                    temp = node.left
                if node.right:
                    temp = node.right
                del node
                return temp
            else:
                # node with two children
                # get inorder successor i.e smallest in the right subtree
                temp = self.getMinNode(node.right)
                node.key = temp.key
                node.right = self.delete(node.right, temp.key)

        node.height = max(self.height(node.left), self.height(node.right)) + 1

        balance = self.get_balance(node)

        # Left Left imbalance
        if balance > 1 and key < node.left.key:
            return self.rightRotate(node)

        # Right Right imbalance
        if balance < -1 and key > node.right.key:
            return self.leftRotate(node)

        # Left Right imbalance
        if balance > 1 and key > node.left.key:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        # Right left imbalance

        if balance < -1 and key < node.right.key:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def getMinNode(self, node):
        if not node:
            return node

        if node.left:
            return self.getMinNode(node.left)

        return node

    def preorder(self, node):
        if not node:
            return
        print(node.key)
        self.preorder(node.left)
        self.preorder(node.right)

    def findMax(self, node):
        if not node:
            return -float('inf')
        return max(node.key, self.findMax(node.left), self.findMax(node.right))


def max_of_subarrays(arr, n, k):
    result = []
    i = 0
    tree = AVLTree()
    root = None
    while i < k:
        root = tree.insert(root, arr[i])
        i += 1
    result.append(tree.findMax(root))
    while i < n:
        root = tree.delete(root, arr[i - k])
        root = tree.insert(root, arr[i])
        result.append(tree.findMax(root))
        i += 1

    return result


if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    # print('Outlier:', arr[39:(39 + 122)])
    expectedResult = list(map(int, input().split()))
    result = max_of_subarrays(arr, len(arr), k)
    # print("Length of result :", len(result))
    for i, item in enumerate(result):
        assert item == expectedResult[i], f'match break at index {i}'
    print(result)

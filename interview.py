class Node():
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def make_tree(this_arr, shoot, i, n):
    if i < n:
        temp = Node(this_arr[i])
        shoot = temp

        shoot.left = make_tree(this_arr, shoot.left, 2 * i + 1, n)
        shoot.right = make_tree(this_arr, shoot.right, 2 * i + 2, n)

    return shoot


def invert_tree(froot):
    if froot:
        invert_tree(froot.left)
        invert_tree(froot.right)
        froot.left, froot.right = froot.right, froot.left


def dfs_tree(boot: Node):
    if boot:
        dfs_tree(boot.left)
        print(boot.data, end=' ')
        dfs_tree(boot.right)


if __name__ == '__main__':
    arr = [1,2,3,4]
    n = len(arr)
    root = None
    root = make_tree(arr, root, 0, n)
    dfs_tree(root)
    invert_tree(root)
    print('\n')
    dfs_tree(root)
    invert_tree(root)
    print('\n')
    dfs_tree(root)

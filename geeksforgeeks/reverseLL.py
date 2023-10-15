class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def createLL(arr):
    n = len(arr)
    root = Node(arr[0])
    curr = Node()
    curr.next = root
    curr = curr.next
    for i in range(1, n):
        curr.next = Node(arr[i])
        curr = curr.next

    return root


def traverseLL(root):
    if not root:
        return

    temp = Node()
    temp.next = root
    temp = temp.next

    while temp:
        print(temp.val, end='->')
        temp = temp.next


def reverseLL(root):
    if not root or not root.next:
        return root

    newRoot = reverseLL(root.next)
    root.next.next = root
    root.next = None

    return newRoot


def reverseLLIter(root):  # todo
    if not root:
        return root

    # 1->2->3->4->
    #
    # temp = Node()
    # temp.next = root
    # temp = temp.next
    prev, curr, nxt = None, root, root

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


def groupReverse(root, k):  # Reverse LL in a group of k
    if not root or not root.next:
        return root
    # 1->2->3->4->5->6->7->8
    # k=3
    # 3->2->1->6->5->4->8->7
    prev, curr, nxt = None, root, root
    i = 0
    while curr and i < k:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        i += 1

    root.next = groupReverse(nxt, k)

    return prev


def detectLoop(head):
    # code here
    fast, slow = head, head

    # check loop
    while True:
        if not fast or not slow:
            return False

        if fast.next:
            fast = fast.next.next
        else:
            return False
        if slow:
            slow = slow.next
        else:
            return False

        if fast == slow:
            return True

def deleteLoop(head):
    fast, slow, trail = head, head, head

    # check loop
    while True:
        if not fast or not slow:
            break

        if fast.next:
            fast = fast.next.next
        else:
            break
        if slow:
            trail = slow
            slow = slow.next
        else:
            break

        if fast == slow:
            break
    if trail != head:
        trail.next = None



if __name__ == '__main__':
    arr = [9, 34, 69, 82, 0, 3, 70]
    root = createLL(arr)
    root = groupReverse(root, 4)
    traverseLL(root)
    # newRoot = reverseLLIter(root)
    # traverseLL(newRoot)

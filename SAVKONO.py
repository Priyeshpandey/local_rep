import heapq


def get_max_heap(arr):  # O(3n)
    arr = [-1 * arr[i] for i in range(len(arr))]
    heapq.heapify(arr)
    return arr


def get_top(arr):
    return -1 * arr[0]


def replace_top(heap, item):
    new_item = heapq.heapreplace(heap, -1 * item)
    return -1 * new_item


t = int(input())

for i in range(t):
    n, z = map(int, input().split())
    sol = list(map(int, input().split()))
    heap = get_max_heap(sol)    # O(n)
    attack = 0
    attacker = get_top(heap) #O(1)
    while z > 0 and attacker > 0: #(no. of attacks)
        z -= attacker
        attack += 1
        attacker //= 2
        replace_top(heap, attacker) #O(log(n))
        attacker = get_top(heap)    #O(1)

    print(attack if z <= 0 else 'Evacuate')

#net = O(n) + O(k*logn)
class Diamond(object):
    def __init__(self, a, w, v):
        self.a = a
        self.w = w
        self.v = v
        self.ratio = v // w

    def add(self, val):
        self.a += val

    def remove(self, val):
        self.a -= val


n, q = map(int, input().split())
diamond = []

for i in range(n):
    a, w, v = map(int, input().split())
    diamond.append(Diamond(a, w, v))

# queries
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        pos = query[2]
        num = query[1]
        diamond[pos-1].add(num)
    elif query[0] == 2:
        pos = query[2]
        num = query[1]
        diamond[pos - 1].remove(num)
    else:
        weight = query[1]
        # greedy knapsack logic


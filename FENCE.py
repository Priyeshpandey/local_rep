t = int(input())

for _ in range(t):
    n, m, k = map(int,input().split())
    points = set()
    for i in range(k):
        x, y = map(int, input().split())
        points.add((x, y))
    fence = k*4
    for x, y in points: # O(K)
        up = (x-1, y)
        down = (x+1, y)
        left = (x, y-1)
        right = (x, y+1)
        neighbors = [up, down, left, right]

        for neighbor in neighbors:
            if neighbor in points:
                fence -= 1
    print(fence)
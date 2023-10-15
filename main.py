from typing import List
from collections import deque


# 1 <= deadends.length <= 500
# deadends[i].length == 4
# target.length == 4
# target will not be in the list deadends.
# target and deadends[i] consist of digits only.

class Solution:
    def getNeighbors(self, deadends, target):
        if target in deadends:
            return []
        lock = [x for x in target]
        neighbors = []
        for i in range(4):
            x = int(lock[i])
            prev = (x - 1) % 10
            next = (x + 1) % 10
            new_lock = ''.join(lock[:i] + [str(prev)] + lock[i + 1:])
            if new_lock not in deadends:
                neighbors.append(new_lock)
            new_lock = ''.join(lock[:i] + [str(next)] + lock[i + 1:])
            if new_lock not in deadends:
                neighbors.append(new_lock)

        return neighbors

    def openLock(self, deadends: List[str], target: str) -> int:
        if target in deadends or "0000" in deadends:
            return -1
        q = deque()
        q.append(("0000", 0))
        visited = [0 for _ in range(10000)]
        while q:
            pos, count = q.popleft()
            visited[int(pos)] = 1
            neighbors = self.getNeighbors(deadends, pos)
            for neighbor in neighbors:
                if visited[int(neighbor)] == 0 and neighbor not in deadends:
                    if neighbor == target:
                        return count + 1
                    q.append((neighbor, count + 1))
        return -1


if __name__ == '__main__':
    obj = Solution()
    deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    target = "8888"
    print(obj.openLock(deadends, target))

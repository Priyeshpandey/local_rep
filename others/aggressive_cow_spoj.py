t = int(input())  # number of TCs


class Sol:
    def findSol(self, arr, n, c):
        arr.sort()
        if n < c:
            return -1
        dist = []
        for i in range(1,n):
            dist.append(arr[i] - arr[i-1])

        if n == c:
            return min(dist)

        start = min(dist)
        end = arr[-1] - arr[0]
        res = -1
        while start <= end:
            mid = start + (end-start)//2

            if self.isValid(dist,n,c,mid):
                res = mid
                start = mid + 1
            else:
                end = mid - 1

        return res

    def isValid(self, dist, n, c, safety):  #[2,3,1,4,3] # safety=6
        sum_=0
        count = 1
        for i in range(n-1):
            if sum_ < safety:
                sum_+=dist[i]
            else:
                count+=1
                sum_=dist[i]
                if count >=c:
                    return True
        if sum_ >= safety:
            count+=1
        return False if count < c else True


for _ in range(t):
    n, c = map(int, input().split())  # n stalls, c cows
    stalls = []
    for i in range(n):
        loc = int(input())
        stalls.append(loc)
    sol = Sol()
    print(sol.findSol(stalls, n, c))

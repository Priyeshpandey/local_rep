T = int(input())

for _ in range(T):
    N = int(input())
    salary = list(map(int, input().split()))
    print(sum(salary)-min(salary)*len(salary))

T = int(input())

def get_safe_house_count(house_range, diff):
    # (0,1), (1,2), (2,4), (4,8), (8,-1)
    count = 0
    start, end = house_range
    if start == 0:
        if end > diff:
            count+=end-diff-1
    elif end == -1:
        if start + diff < 100:
            count+=100-start-diff
    else:
        if end - start > 2*diff:
            count+= end -start - 2*diff-1
    return count
for _ in range(T):
    M, x, y = map(int,input().split())
    diff = x*y
    cops_house = list(map(int,input().split()))
    cops_house.sort()
    count = get_safe_house_count((0,cops_house[0]), diff)
    count += get_safe_house_count((cops_house[-1], -1), diff)
    for num in range(1,M):
        count+=get_safe_house_count((cops_house[num-1],cops_house[num]), diff)
    print(count)

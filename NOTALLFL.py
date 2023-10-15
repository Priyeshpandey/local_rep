t = int(input())


def get_distinct_flav_count(arr, start, end, flav_count, flav, end_flag, start_flag):
    if start_flag==1:
        flav[arr[start-1]] -= 1
        if flav[arr[start-1]] == 0:
            flav_count -= 1
    if end_flag:
        if arr[end] not in flav or flav[arr[end]] == 0:
            flav[arr[end]] = 1
            flav_count += 1
        else:
            flav[arr[end]] += 1
    return flav_count, flav


for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    flav={}
    flav_count=0
    max_seg_len=0
    seg_len=0
    start=0
    end=0
    end_flag=1
    start_flag=0
    while end < n:
        flav_count, flav = get_distinct_flav_count(arr,start,end,flav_count,flav,end_flag=end_flag,start_flag=start_flag)
        if flav_count < k:
            # Valid segment
            seg_len = end - start + 1
            if seg_len > max_seg_len:
                max_seg_len = seg_len
            end_flag=1
            start_flag=0
            end+=1
        else:
            start_flag=1
            end_flag=0
            start+=1
    print(max_seg_len)
def smallestSubWithSum(arr, n, target):
    # Your code goes here
    sum_ = 0
    start, end = 0, 0
    min_len = n
    while end < n:
        while end < n and sum_ <= target:
            print(sum_, start, end)
            sum_ += arr[end]
            end += 1
        end -= 1
        min_len = min(min_len, end - start + 1)
        while start <= end < n and sum_ > target:
            print(sum_, start, end)
            min_len = min(min_len, end - start + 1)
            sum_-=arr[start]
            start+=1

        end+=1

    return min_len


if __name__ == '__main__':
    arr = [6, 3, 4, 5, 4, 3, 7, 9]
    print(arr)
    n = len(arr)
    x = 16

    print(smallestSubWithSum(arr, n, x))

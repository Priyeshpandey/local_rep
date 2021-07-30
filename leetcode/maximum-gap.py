def bucket_sort(nums):
    bucket = [[] for _ in range(10)]
    B = 10

    for b in range(B):
        for i in range(len(nums)):
            k = (nums[i] // (10 ** b))%10
            bucket[k].append(nums[i])
        i = 0
        # print(bucket)
        for item in bucket:
            for ele in item:
                nums[i] = ele
                i += 1
        bucket = [[] for _ in range(10)]
    return nums


if __name__=='__main__':
    nums = [3470,921,38,741,293,78]
    print(nums)
    print(bucket_sort(nums))
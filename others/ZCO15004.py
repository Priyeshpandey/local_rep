n = int(input()) #O(n)
Y = 500
X = 100000
points = []
for _ in range(n):  #O(n)
    x, y = map(int, input().split())
    points.append((x, y))

points.sort()   #O(nlogn)


# points.append((X, Y))

def get_left_bound_array(arr, n):   #O(max_stack_len*n) ~ O(n)ish
    bound = [(0, -1)]
    stack = []
    stack_len = 0
    for i in range(n):
        if stack_len > 0:
            while stack_len > 0 and stack[-1][1] >= arr[i][1]:
                stack.pop()
                stack_len -= 1
            bound.append(stack[-1] if stack_len > 0 else (0, -1))
        stack.append(arr[i])
        stack_len += 1
    return bound


def get_right_bound_array(arr, n):#O(max_stack_len*n) ~ O(n)ish
    bound = [(X, -1)]
    stack = []
    stack_len = 0
    for i in range(n - 1, -1, -1):
        if stack_len > 0:
            while stack_len > 0 and stack[-1][1] >= arr[i][1]:
                stack.pop()
                stack_len -= 1
            bound.append(stack[-1] if stack_len > 0 else (X, -1))
        stack.append(arr[i])
        stack_len += 1
    bound.reverse()
    return bound


def sanity_max(arr, n): #O(n)
    max_area = 0
    for i in range(n - 1):
        x1 = arr[i][0]
        x2 = arr[i + 1][0]
        max_area = max((x2 - x1) * Y, max_area)

    return max_area


max_area = sanity_max(points, n)    #O(n)
# max_area = 0
left_bound = get_left_bound_array(points, n)    #O(n)
right_bound = get_right_bound_array(points, n)  #O(n)

for i in range(n):  #O(n)
    x1 = left_bound[i][0]
    x2 = right_bound[i][0]
    y = points[i][1]
    max_area = max(max_area, (x2 - x1) * y)
left_area = Y * (points[0][0]) #O(1)
right_area = Y * (X - points[-1][0])    #O(1)
max_area = max(left_area, right_area, max_area) #O(1)
print(max_area) #O(1)

# Total = O(6*n + nlogn + k) n = 10^5 => ~ 10^6 ~ 1s bcz 1s~ 10^8 ish

# if __name__ == '__main__':
#     arr = [2, 7, 5, 4, 1, 3, 9]
#     n = len(arr)
#     left_bound = get_left_bound_array(arr, n)
#     right_bound = get_right_bound_array(arr, n)
#     print(arr)
#     print(left_bound)
#     print(right_bound)

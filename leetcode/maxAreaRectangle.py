# https://www.geeksforgeeks.org/maximum-size-rectangle-binary-sub-matrix-1s/

from leetcode.custom_lib import binary_matrix_generator, printMatrix, generate_matrix_from_string


def get_max_hist(arr):
    n = len(arr)
    stack = []
    leftBound = [0] * n
    rightBound = [0] * n
    for i in range(n):
        if not stack or arr[stack[-1]] < arr[i]:
            leftBound[i] = i
            stack.append(i)
        else:
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            leftBound[i] = stack[-1] + 1 if stack else 0
            stack.append(i)
    stack.clear()
    for i in range(n - 1, -1, -1):
        if not stack or arr[stack[-1]] < arr[i]:
            rightBound[i] = i
            stack.append(i)
        else:
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            rightBound[i] = stack[-1] - 1 if stack else n - 1
            stack.append(i)

    # print(leftBound, rightBound, sep='\n')

    maxArea = 0
    for i in range(n):
        area = arr[i] * (rightBound[i] - leftBound[i] + 1)
        maxArea = max(maxArea, area)

    return maxArea


def max_area_rectangle(matrix):
    # use max_area_under_histogram as subroutine and calculate max_area histogram for each row as base and keep
    # track of max_area
    rows = len(matrix)
    cols = len(matrix[0])
    max_area = get_max_hist(matrix[0])
    for i in range(1, rows):
        matrix[i] = [matrix[i][j]+matrix[i-1][j] if matrix[i][j] else 0 for j in range(cols)]
        max_area = max(max_area,get_max_hist(matrix[i]))

    return max_area


if __name__ == '__main__':
    r, c = 5, 4
    matrix = binary_matrix_generator(r, c)
    printMatrix(matrix)
    print("-" * 20)
    print(max_area_rectangle(matrix))

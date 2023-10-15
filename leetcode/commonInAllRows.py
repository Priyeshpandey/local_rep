# https://www.geeksforgeeks.org/common-elements-in-all-rows-of-a-given-matrix/
from leetcode.custom_lib import printMatrix, randomMatrixGenerator
def commonElements(matrix: list[list[int]]) -> list[int]:
    n, m = len(matrix), len(matrix[0])
    record = {}

    for i in range(n):
        lookup = set()
        for j in range(m):
            if matrix[i][j] in lookup:
                continue
            if matrix[i][j] in record:
                record[matrix[i][j]] += 1
            else:
                record[matrix[i][j]] = 1
            lookup.add(matrix[i][j])
    print(record)
    result = [key for key, val in record.items() if val == n]

    return result


if __name__=="__main__":
    matrix = randomMatrixGenerator(5, 5, 1, 3)
    printMatrix(matrix)
    print(commonElements(matrix))
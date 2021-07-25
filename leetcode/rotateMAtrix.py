# todo
def rotate(matrix):
    n = len(matrix)

    for i in range(n//2):
        for j in range(n-1):
            matrix[i][j], matrix[j][n-j-1], \
            matrix[n-i-1][n-j-1], matrix[n-j-1][j] = \
                matrix[n - j - 1][j], matrix[i][j], matrix[j][n - j - 1], \
                matrix[n - i - 1][n - j - 1]


if __name__=='__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    for row in matrix:
        print(*row, sep='\t')

    rotate(matrix)
    print("="*50)
    for row in matrix:
        print(*row, sep='\t')
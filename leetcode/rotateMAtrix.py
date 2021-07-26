# Done
def rotate(matrix):
    n = len(matrix)

    for i in range(n//2):
        for j in range(i,n-i-1):
            matrix[i][j], matrix[j][n-i-1], \
            matrix[n-i-1][n-j-1], matrix[n-j-1][i] = matrix[n-j-1][i], matrix[i][j],\
                                                     matrix[j][n-i-1],matrix[n-i-1][n-j-1]


if __name__=='__main__':
    matrix = [[1,2,3,4],[4,5,6,7],[7,8,9,10], [3,5,1,12]]
    for row in matrix:
        print(*row, sep='\t')

    rotate(matrix)
    print("="*50)
    for row in matrix:
        print(*row, sep='\t')
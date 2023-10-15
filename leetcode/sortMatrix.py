

def sortedMatrix(N,Mat):
    merge = []
    for row in Mat:
        merge+=row
    merge.sort()
    for i in range(N):
        for j in range(N):
            matrix[i][j] = merge[i*N+j]
    return matrix




if __name__=='__main__':
    matrix = [[1,2,3],[1,2,3],[1,2,3]]
    sortedMatrix(3, matrix)

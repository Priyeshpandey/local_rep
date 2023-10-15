def nPr(n, r):
    # P(n, r) = P(n-1, r) + r*P(n-1, r-1)
    X = 10**9 + 7
    P = [[0]*(r+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(r+1):
            if i < j:
                P[i][j] = 0
            elif j==0:
                P[i][j] = 1
            else:
                P[i][j] = P[i-1][j] + j*P[i-1][j-1]

    return P[n][r]%X



def nCr(N, R):
    X = 10**9 + 7
    C = [[0]*(R+1) for _ in range(N+1)]

    for n in range(N+1):
        for r in range(R+1):
            if r > n:
                C[n][r] = 0
            elif (r == 0) or (r == n):
                C[n][r] = 1
            elif r == 1:
                C[n][r] = n
            else:
                C[n][r] = C[n-1][r-1] + C[n-1][r]

    return C[N][R]%X



if __name__ == '__main__':
    print(nPr(10, 10))
    print(nCr(15,5))
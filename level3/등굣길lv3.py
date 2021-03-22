def solution(m, n, puddles):

    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                dp[i][j] = 1
            elif [j, i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                dp[i][j] %= 1000000007  

    return dp[n][m]

m = 4
n = 3
puddles = [[2,2]]
print(solution(m, n, puddles))
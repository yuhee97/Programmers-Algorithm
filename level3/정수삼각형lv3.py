def solution(triangle):

    n = len(triangle)
    dp = [[0] * i for i in range(1, n+1)]

    for i in range(n):
        for j in range(len(dp[i])):
            if i == 0 and j == 0:
                dp[0][0] = triangle[0][0]
            elif j == 0 or j == i:
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                else:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

    return max(dp[n-1])

t = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5], [4, 5, 2, 6, 5, 7]]
print(solution(t))

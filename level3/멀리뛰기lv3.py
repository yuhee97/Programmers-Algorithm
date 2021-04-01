def solution(n):
    dp = [0] * (n+1); dp[1] = 1
    for i in range(2, n+1):
        if i == 2:
            dp[i] = 2
            continue
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= 1234567
    return dp[n]

n = 10
print(solution(n))
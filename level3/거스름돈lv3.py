def solution(n, money):
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(len(money)):
        for j in range(money[i], n+1):
            dp[j] += dp[j-money[i]]
            dp[j] %= 1000000007
    return dp[n]

n = 5
money = [1, 2, 5]
print(solution(n. money))
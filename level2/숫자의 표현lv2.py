def solution(n):
    c = 0
    for i in range(1, n+1):
        SUM = 0; j = i
        while SUM <= n:
            SUM += j
            j += 1
            if SUM == n:
                c += 1
    return c

nn = 10000
print(solution(nn))
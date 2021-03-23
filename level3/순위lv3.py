def solution(n, results):
    g = [[0] * n for _ in range(n)]

    for r in results:
        a, b = r[0], r[1]
        g[a-1][b-1] = 1
        g[b-1][a-1] = -1

    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if g[i][k] + g[k][j] == -2:
                    g[i][j] = -1
                if g[i][k] + g[k][j] == 2:
                    g[i][j] = 1

    c = 0
    for i in range(n):
        check = True
        for j in range(n):
            if i != j:
                if g[i][j] == 0:
                    check = False
                    break
        if check:
            c += 1

    return c


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))
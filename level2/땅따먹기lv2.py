def solution(land):
    n = len(land)
    g = [[0] * 4 for _ in range(n)]
    for i in range(n):
        for j in range(4):
            if i == 0 :
                g[i][j] = land[i][j]
            else:
                v = 0
                for k in range(4):
                    if k != j:
                        if v < g[i-1][k]:
                            v = g[i-1][k]
                g[i][j] = land[i][j] + v
                
    return max(g[n-1])
        
land =[[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))
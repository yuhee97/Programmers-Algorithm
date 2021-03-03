from collections import deque

def bfs(graph, num):
    queue = deque()
    visited = [0] * num; c = 0
    for i in range(num):
        if visited[i] == 0:
            c += 1
            queue.append(i)
            while queue:
                x = queue.popleft()
                for j in graph[x]:
                    if visited[j] == 0:
                        queue.append(j)
                        visited[j] = 1
    return c
                        
    
def solution(n, computers):
    g = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                if computers[i][j] == 1:
                    g[i].append(j)
    result = bfs(g, n)
    return result

nn = 3
coms = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(nn, coms))
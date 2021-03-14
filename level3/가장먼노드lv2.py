import heapq

def dijkstra(distance, g):
    q = []
    heapq.heappush(q, [0, 1])
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in g[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])
    return distance

def solution(n, edge):
    INF = int(1e9); d = [INF] * (n+1); d[0] = 0; c = 0
    graph = [[] for _ in range(n+1)]
    for i in edge:
        graph[i[0]].append((i[1], 1))
        graph[i[1]].append((i[0], 1)) 

    v = dijkstra(d, graph)
    for i in range(1, n+1):
        if max(v) == v[i]:
            c+=1
    return c

nn = 6
e = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	
print(solution(nn, e))
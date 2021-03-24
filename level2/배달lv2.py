import heapq

INF = int(1e9)

def dijkstra(n, g):
    distance = [INF] * (n+1)
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

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    for i in road:
        a, b, c = i[0], i[1], i[2]
        graph[a].append([b, c])
        graph[b].append([a, c])
    g = dijkstra(N, graph); c = 0
    for i in g:
        if i <= K:
            c += 1
    return c

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
print(solution(N, road, K))

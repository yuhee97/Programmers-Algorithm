import heapq

def solution(n, works):
    q = []; result = 0
    for work in works:
        heapq.heappush(q, -work)
    while n!=0:
        v = heapq.heappop(q)
        if v == 0:
            break
        n-=1
        heapq.heappush(q, v+1)
    for i in q:
        result += i**2
    return result

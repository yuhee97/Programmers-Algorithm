import heapq

def solution(scoville, K):
    
    q = []; check = False
    for i in range(len(scoville)):
        heapq.heappush(q, scoville[i])
    c = 0
    
    while q:
        x1 = heapq.heappop(q)
        if x1 < K:
            if q:
                x2 = heapq.heappop(q)
                heapq.heappush(q, x1 + x2*2)
                c += 1
        else:
            check = True
            break
    
    if check:
        return c
    else:
        return -1
        
sco = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(sco, k))
import heapq

def solution(operations):
    q_max = []; q_min = []
    for i in range(len(operations)):
        if operations[i][0] == "I":
            heapq.heappush(q_max, -int(operations[i][2:]))
            heapq.heappush(q_min, int(operations[i][2:]))
        elif operations[i] == "D 1":
            if q_max:
                v = heapq.heappop(q_max)
                q_min.remove(-v)
        else:
            if q_min:
                v = heapq.heappop(q_min)
                q_max.remove(-v)

    if q_max:
        return [-heapq.heappop(q_max), heapq.heappop(q_min)]
    else:
        return [0, 0]

operations = ["I 7","I 5","I -5","D -1"]
print(solution(operations))
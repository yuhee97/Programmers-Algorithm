def solution(bridge_length, weight, truck_weights):
    result = 0
    q = [0] * bridge_length
    
    while truck_weights:
        q.pop(0)
        if sum(q) + truck_weights[0] <= weight:
            q.append(truck_weights.pop(0))
        else:
            q.append(0)
        result += 1
        
    return result + len(q)


b_l = 2
w = 10
t_w = [7, 4, 5, 6]
print(solution(b_l, w, t_w))

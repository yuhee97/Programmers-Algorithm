def solution(d, budget):
    lis = sorted(d); c = 0
    for i in range(len(d)):
        if budget - lis[i] >= 0:
            budget -= lis[i]
            c+=1
        else:
            break
    return c


d = [1,2,4,56,2,34,54]
budget = 100
print(solution(d, budget))
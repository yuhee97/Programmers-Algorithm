def solution(n, lost, reserve):
    for i in range(1, n+1):
        if i in lost:
            if i in reserve:
                reserve.remove(i)
                lost.remove(i)
    for i in range(1, n+1):
        if i in lost:
            if (i-1) in reserve:
                reserve.remove(i-1)
                lost.remove(i)
                continue
            elif (i+1) in reserve:
                reserve.remove(i+1)
                lost.remove(i)
            else:
                continue           
    return n - len(lost)

nn = 5
lost_ = [2, 4]
reserve_ = [1, 3, 5]
print(solution(nn, lost_, reserve_))
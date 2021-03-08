def solution(x, n):
    v = 0; result = []; c = 1
    while c <= n:
        v += x
        result.append(v)
        c += 1
    return result
        

xx = 10
nn = 8
print(solution(10, 8))

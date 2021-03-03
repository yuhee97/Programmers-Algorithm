def solution(n, m): # 유클리드 호제법 이용
    nm = max(n, m); mm = min(n, m); r = 1; result = []
    while r > 0:
        r = nm % mm
        nm = mm
        mm = r
    result.append(nm)
    result.append(n*m//nm)
    return result

n = 12
m = 3
print(solution(n, m))
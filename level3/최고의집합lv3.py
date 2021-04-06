def solution(n, s):
    if n > s:
        return [-1]
    result = []
    while s != 0:
        mod = s // n
        result.append(mod)
        n -= 1
        s -= mod
    return result

n = 2
s = 9
print(solution(n, s))
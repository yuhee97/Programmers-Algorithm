def solution(n):
    n_3 = ''; result = 0
    while n != 0:
        r = n % 3
        n = n // 3
        n_3 += str(r)
    for i in range(len(n_3)-1, -1, -1):
        result += int(n_3[i]) * 3**(len(n_3)-i-1)
    return result

n = 45
print(solution(n))
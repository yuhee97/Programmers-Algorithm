def solution(n):
    num = list(map(int, str(n)))
    num.sort(reverse = True)
    strr = ''
    for i in num:
        strr += str(i)
    return int(strr)

n = 78295923
print(solution(n))
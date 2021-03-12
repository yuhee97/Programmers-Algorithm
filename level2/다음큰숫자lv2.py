def check(num):
    c = 0
    while True:
        r = num % 2
        num = num // 2
        if num == 0 and r == 1:
            return c+1
        if r == 1:
            c += 1
            
def solution(n):
    first = check(n)
    for i in range(n+1, 1000001):
        if check(i) == first:
            return i

nn = 78
print(solution(nn))
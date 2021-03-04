import math

def check(number):
    if number == 2:
        return True
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True


def solution(n):
    c = 0
    for k in range(2, n+1):
        if check(k):
            c += 1
    return c

nn = 1000000
print(solution(nn))
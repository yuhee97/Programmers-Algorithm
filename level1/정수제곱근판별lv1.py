import math

def solution(n):
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            if n // i == i:
                return (i+1)**2
    return -1

n = 121
print(solution(n))
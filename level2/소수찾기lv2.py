from itertools import permutations
import math

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    num = []; c = 0
    for i in range(1, len(numbers)+1):
        for j in list(permutations(numbers, i)):
            num.append(int(''.join(j)))
    for k in list(set(num)):
        if isPrime(k):
            c += 1

    return c


nn = '9898211'
print(solution(nn))
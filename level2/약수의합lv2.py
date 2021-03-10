import math

def solution(n):
    result = []
    
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            result.append(i)
            if i != n//i:
                result.append(n//i)
            
    return sum(result)

nn = 20
print(solution(nn))
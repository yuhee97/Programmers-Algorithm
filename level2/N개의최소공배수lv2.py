import math
    
def solution(arr):
    n = arr[0]
    for i in range(1, len(arr)):
        v = math.gcd(n, arr[i])
        result = v * (n//v)* (arr[i]//v)
        n = result
    return result

arrr = [2,6,8,14]
print(solution(arrr))
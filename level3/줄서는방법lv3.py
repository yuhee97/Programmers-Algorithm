import math

def solution(n, k):
    entire = math.factorial(n)
    case = entire//n; result = []; r = k
    num = [i for i in range(1, n+1)]
    while len(num)>1:
        mod = (r-1) // case
        r %= case
        result.append(num.pop(mod))
        case //= len(num)
    result.append(num.pop(0))
    return result
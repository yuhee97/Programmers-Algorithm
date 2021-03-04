from collections import Counter

def solution(clothes):
    result = 1
    case = Counter([kind for name, kind in clothes])
    for i in case.values():
        result *= i+1
    return result-1

c = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(c))

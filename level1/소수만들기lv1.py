from itertools import combinations
import math

def check(value):
    for i in range(2, int(math.sqrt(value))+1):
        if value % i == 0:
            return False
    return True

def solution(nums):
    combis = list(combinations(nums, 3))
    result = 0
    for combi in combis:
        v = sum(combi)
        if check(v):
            result += 1
    return result


nums = [1,2,3,4,5]
print(solution(nums))
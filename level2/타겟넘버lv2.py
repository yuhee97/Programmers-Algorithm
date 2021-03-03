result = []

def dfs(nums, st, s):
    if st == len(nums):
        result.append(s)
        return
    dfs(nums, st+1, s + nums[st])
    dfs(nums, st+1, s - nums[st])
    
def solution(numbers, target):
    c = 0
    dfs(numbers, 0, 0)
    for i in range(len(result)):
        if result[i] == target:
            c += 1
    return c

ns = [1, 1, 1, 1, 1]
t = 3
print(solution(ns, t))
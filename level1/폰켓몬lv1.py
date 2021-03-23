def solution(nums):
    n = len(nums) // 2
    num = set(nums)
    if len(num) <= n:
        return len(num)
    return n

nums = [1,23,4,2,1]
print(solution(nums))
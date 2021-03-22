def solution(n, times):
    left = 1; right = n * max(times)
    t = times; t.sort()
    result = []
    while left <= right:
        mid = (left + right) // 2
        v = n
        for i in t:
            v -= mid // i
            if v <= 0:
                break  
        if v <= 0:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

n = 10
times = [3,4,8]
print(solution(n, times))
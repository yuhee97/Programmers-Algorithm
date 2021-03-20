import heapq

def solution(jobs):
    n = len(jobs); i = 0
    disk = sorted(jobs, key = lambda x:x[0])
    q = []; result = 0; start = disk[0][0]
    while i <= len(jobs):
        if i < len(jobs) and disk[i][0] <= start:
            heapq.heappush(q, [disk[i][1], disk[i][0]])
            i += 1
        else:
            if q:
                ms, st = heapq.heappop(q)
                start += ms
                result += (start - st)
                if i == len(jobs) and not q:
                    break
            else:
                start += 1

    return result//len(jobs)

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
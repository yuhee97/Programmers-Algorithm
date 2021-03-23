from collections import Counter

def solution(N, stages):

    n = [[0] * 2 for _ in range(N)]
    stage_n = Counter(stages)
    num = len(stages); result = []

    for i in range(0, N):
        n[i][0] = i+1
        if stage_n[i+1]:
            n[i][1] = stage_n[i+1]/num
            num -= stage_n[i+1]
        else:
            n[i][1] = 0

    n_lis = sorted(n, key = lambda x:(-x[1], x[0]))

    for i in n_lis:
        result.append(i[0])   

    return result

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
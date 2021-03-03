def solution(progresses, speeds):
    result = []
    v_lis = []

    for i in range(len(speeds)):
        v = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] != 0:
            v += 1
        v_lis.append(v)

    if len(v_lis) == 1:
        return [1]

    for j in range(len(v_lis)):
        if j == 0:
            out = v_lis[j]
            c = 1
        else:
            if out >= v_lis[j]:
                c += 1
            else:
                result.append(c)
                out = v_lis[j]
                c = 1

    result.append(c)
    return result

p = [93, 30, 55]
s = [1, 30, 5]
print(solution(p, s))
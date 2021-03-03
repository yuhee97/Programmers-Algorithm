def solution(answers):
    one = [1, 2, 3, 4, 5] * 2000
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    c = [0] * 3; result = []
    for i in range(len(answers)):
        if one[i] == answers[i]:
            c[0] += 1
        if two[i] == answers[i]:
            c[1] += 1
        if three[i] == answers[i]:
            c[2] += 1
    mx = max(c)
    if mx == c[0]:
        result.append(1)
    if mx == c[1]:
        result.append(2)
    if mx == c[2]:
        result.append(3)
        
    return result

answer = [1,2,3,4,5]
print(solution(answer))
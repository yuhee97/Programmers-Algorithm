def solution(people, limit):

    result = 0; p = people; p.sort()
    start = 0; end = len(p)-1

    while start <= end:
        if p[start] + p[end] <= limit:
            result += 1
            start += 1
            end -= 1
        else:
            result += 1
            end -= 1

    return result

p = [10, 20, 30, 30, 40]
l = 40
print(solution(p, l))
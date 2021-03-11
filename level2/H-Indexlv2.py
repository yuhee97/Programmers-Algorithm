def solution(citations):
    result = 0
    for i in range(10001):
        down = 0; up = 0;
        for j in range(len(citations)):
            if i <= citations[j]:
                up += 1
            else:
                down += 1
                
        if i <= up and len(citations)-up == down:
            if result < i:
                result = i
                
    return result

c = [3, 0, 6, 1, 5]
print(solution(c))

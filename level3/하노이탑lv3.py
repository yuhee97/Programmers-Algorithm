answer = []

def hanoi(n, start, mid, end):
    if n == 1:
        answer.append([start, end])
        return
    else:
        hanoi(n-1, start, end, mid)
        answer.append([start, end])
        hanoi(n-1, mid, start, end)
        
def solution(n):
    hanoi(n, 1, 2, 3)
    return answer

n = 5
print(solution(n))
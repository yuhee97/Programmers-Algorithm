from collections import deque

def solution(priorities, location):
    c = 0
    q = deque()
    for i in range(len(priorities)):
        q.append([priorities[i], i])
    while q:
        check = False
        for h in range(1, len(q)):
            if q[0][0] < q[h][0]:
                check = True
                q.append([q[0][0], q[0][1]])
                q.popleft()
                break
        if not check:
            if q[0][1] == location:
                return c+1
            else:
                c += 1
                q.popleft()


p = [2, 1, 3, 2]
l = 2
print(solution(p, l))

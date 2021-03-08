from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(order):
    q = deque(); i = 0; c = 0
    visited = [[[0] for _ in range(11)] for _ in range(11)]
    q.append([5, 5])
    while q:
        x, y = q.popleft()
        if i > len(order)-1:
            break
        if order[i] == 'U':
            nx, ny  = x + dx[0], y + dy[0]
        elif order[i] == 'L':
            nx, ny  = x + dx[1], y + dy[1]
        elif order[i] == 'D':
            nx, ny  = x + dx[2], y + dy[2]
        else:
            nx, ny  = x + dx[3], y + dy[3]
        if 0 <= nx < 11 and 0 <= ny < 11:
            q.append([nx, ny]); 
            if [x, y] in visited[nx][ny] or [nx, ny] in visited[x][y]:
                i += 1
                continue
            else:
                visited[nx][ny].append([x, y]); visited[x][y].append([nx, ny])
                c += 1
        else:
            q.append([x, y])
        i += 1
    return c

def solution(dirs):
    v = bfs(dirs)
    return v 

dir = 'UDLRUUUUUULDLDR'
print(solution(dir))

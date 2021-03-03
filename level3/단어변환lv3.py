from collections import deque

def bfs(start, end, g):
    q = deque()
    visited = [0] * (len(g) + 1)
    q.append([0, start])
    while q:
        n, s = q.popleft()
        if s == end:
            return visited[n]
        for w in range(len(s)):
            check_s = s[0:w] + s[w+1:]
            for strr in range(len(g)):
                st = g[strr]
                check_st = st[0:w] + st[w+1:]
                if check_s == check_st:
                    if visited[strr+1] == 0:
                        visited[strr+1] = visited[n] + 1
                        q.append([strr+1, g[strr]])
    return visited
                                       
                
def solution(begin, target, words):
    if target not in words:
        return 0
    else:
        v = bfs(begin, target, words)
        return v


b = "hit"
t = "cog"
w = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(b, t, w))
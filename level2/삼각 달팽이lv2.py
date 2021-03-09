def solution(n):
    N = n*(n+1)//2; result = []
    box = [[0] * i for i in range(1, n+1)]
    dir = 'd'; x, y = -1, 0; c = n
    d = 0; r = 0; u = 0
    for cur in range(1, N+1):
        if dir == 'd':
            d += 1
            x, y = x+1, y
            box[x][y] = cur
            if d == c:
                dir = 'r'
                d = 0
                c -= 1
        elif dir == 'r':
            r += 1
            x, y = x, y+1
            box[x][y] = cur
            if r == c:
                dir = 'u'
                r = 0
                c -= 1
        else:
            u+=1
            x, y = x-1, y-1
            box[x][y] = cur
            if u == c:
                dir = 'd'
                u = 0
                c -= 1
                
    for i in range(len(box)):
        for j in range(len(box[i])):
            result.append(box[i][j])
    
    return result


num = 10
print(solution(num))
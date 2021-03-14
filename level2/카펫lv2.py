import math

def solution(brown, yellow):
    entire = brown + yellow # 전체 격자의 수
    result = []
    for i in range(1, int(math.sqrt(yellow))+1):
        if yellow % i == 0:
            j = yellow // i
            if (entire-yellow) == i*2+(j+2)*2:
                result.extend([j+2, i+2])
                return result
        

b = 10
y = 2
print(solution(b, y))
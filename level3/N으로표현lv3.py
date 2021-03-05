def solution(N, number):
    num = [set() for _ in range(9)]; 
    for i in range(1, 9):
        num[i].add(int(str(N)*i))

    for i in range(1, 9):
        for k in range(1, 9-i):
            for j in num[i]:
                for h in num[k]:
                    num[i+k].add(j+h)
                    num[i+k].add(j-h)
                    num[i+k].add(j*h)
                    if h != 0:
                        num[i+k].add(j//h)

        if number in num[i]:
            return i        
    return -1

n = 5
num = 12
print(solution(n, num))
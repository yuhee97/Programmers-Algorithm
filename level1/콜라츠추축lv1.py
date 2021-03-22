def solution(num):
    i = 0; n = num
    if n == 1:
        return 0
    while i < 500:
        if n % 2 == 0:
            n //= 2
        else:
            n = n*3+1 
        i+= 1
        if n == 1:
            return i
    return -1

num = 17
print(solution(num))
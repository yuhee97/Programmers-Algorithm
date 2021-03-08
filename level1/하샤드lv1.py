def solution(x):
    num = str(x); SUM = 0
    for i in range(len(num)):
        SUM += int(num[i])
    if x % SUM == 0:
        return True
    else:
        return False
        
    
x = 129302
print(solution(x))
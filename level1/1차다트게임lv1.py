def solution(dartResult):
    n = len(dartResult); i = 0; j = 0
    result = [0] * 3
    option = [[] for _ in range(3)]
    while i < n:
        if dartResult[i] == '1':
            if dartResult[i+1] == '0':
                v = 10
                i+=2
            else:
                v = int(dartResult[i])
                i+=1
        else:
            v = int(dartResult[i])
            i+=1
                
        if dartResult[i] == 'S':
            result[j] = v
        elif dartResult[i] == 'D':
            result[j] = v**2
        else:
            result[j] = v**3
        i+=1
        
        if i < n:
            if dartResult[i] == '*':
                option[j].append('*')
                i+=1; j+=1
                continue
            if dartResult[i] == '#':
                option[j].append('#')
                i+=1
        j+=1

    for i in range(3):
        if option[i] != [] and option[i][0] == '*':
            if i == 0:
                result[i] *= 2
            else:
                result[i-1] *= 2
                result[i] *= 2
        elif option[i] != [] and option[i][0] == '#':
            result[i] *= (-1)
        else:
            continue       
    return sum(result)

dd = '1S2D*3T'
print(solution(dd))

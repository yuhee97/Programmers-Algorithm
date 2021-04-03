def solution(s):
    result = []; n = len(s)
    if n == 1:
        return 1
    for i in range(1, n):
        strr = ''
        for j in range(0, n, i):
            if j == 0:
                s_c = s[j:j+i]
                count = 1
            else:
                if j+i < n+1:
                    if s_c == s[j:j+i]:
                        count += 1
                    else:
                        if count < 2:
                            strr += s_c
                        else:
                            strr += (str(count) + s_c)
                        count = 1
                else:
                    strr += s[j:]
                    break
                s_c = s[j:j+i]
                    
        if count == 1:
            strr += s_c
        else:
            strr += (str(count) + s_c)
        result.append(len(strr))   
    return min(result)   

s = "aabbaccc"
print(solution(s))

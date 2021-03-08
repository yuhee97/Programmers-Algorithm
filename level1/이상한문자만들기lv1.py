def solution(s):
    strr = ''; c = 0; i = 0
    while i < len(s):
        if s[i] == ' ':
            strr += s[i]
            i += 1; c = 0
            continue
        if c % 2 == 0: # 짝수번째
            strr += s[i].upper()
            c += 1
        else: # 홀수번째
            strr += s[i].lower()
            c += 1
        i += 1
    return strr
            
ss = "TrY HeLlO WoRlD"
print(solution(ss))
            
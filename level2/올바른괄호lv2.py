def solution(s):
    c1, c2 = 0, 0
    for i in range(len(s)):
        if s[i] == "(":
            c1+=1
        else:
            c2+=1
        if c1 < c2:
            return False
    if c1 != c2:
        return False
    return True
        
    
s = "()()"
print(solution(s))
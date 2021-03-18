def solution(s):
    strr = ""; c = 0
    for i in range(len(s)):
        
        if s[i] == " ":
            strr += s[i]
            c = 0
            continue
            
        if c == 0:
            strr += s[i].upper(); c = 1
            continue   
            
        strr += s[i].lower()

    return strr

ss = "3people unFollowed me"
print(solution(ss))
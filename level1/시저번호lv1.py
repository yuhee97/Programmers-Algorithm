def solution(s, n):
    strr = ''
    for i in range(len(s)):
        if s[i] == ' ':
            strr += s[i]
        elif ord(s[i]) <= 90:
            if ord(s[i]) > 90-n:
                strr += chr(ord(s[i])+n-26)
            else:
                strr += chr(ord(s[i])+n)
        else:
            if ord(s[i]) > 122-n:
                strr += chr(ord(s[i])+n-26)
            else:
                strr += chr(ord(s[i])+n)
    return strr


ss = 'abcz'
nn = 4
print(solution(ss, nn))

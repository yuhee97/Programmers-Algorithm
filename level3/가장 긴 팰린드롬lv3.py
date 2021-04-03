def solution1(s):
    n = len(s); answer = 0
    for i in range(n):
        for j in range(n):
            if i+j >= n:
                continue
            if s[i:i+j+1] == s[i:i+j+1][::-1]:
                if answer < j+1:
                    answer = j+1
    return answer

def solution2(s):
    n = len(s); back_s = ""
    for i in range(n):
        back_s = s[i] + back_s   
    answer = 0
    for i in range(n):
        for j in range(n):
            if i+j >= n:
                continue
            if s[i:i+j+1] == back_s[n-i-j-1:n-i]:
                if answer < j+1:
                    answer = j+1
    return answer
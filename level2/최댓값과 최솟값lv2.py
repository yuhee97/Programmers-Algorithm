def solution(s):
    num = list(map(int, s.split(" ")))
    return str(min(num)) + " " + str(max(num))

ss = "1 2 3 4"
print(solution(ss))
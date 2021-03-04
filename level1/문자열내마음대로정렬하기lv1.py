def solution(strings, n):
    stack = []; result = []
    strings.sort()
    for i in range(len(strings)):
        stack.append([strings[i][n], i])
    stack.sort()
    for i in stack:
        result.append(strings[i[1]])
    return result
        

strr = ["sun", "bed", "car"]
nn = 1
print(solution(strr, nn))
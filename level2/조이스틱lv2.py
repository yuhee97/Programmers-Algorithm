def solution(name):

    now = "A" * len(name); idx = 0; c = 0

    while now!=name:

        if now[idx] != name[idx]:
            first = ord(name[idx]) - ord(now[idx])
            second = ord('Z') - ord(name[idx]) + 1
            c += min(first, second)
            now = now[0:idx] + name[idx] + now[idx+1:]

        if now == name:
            break

        for i in range(1, len(name)):

            if idx+i < len(name) and now[idx+i] != name[idx+i]:
                c += i; 
                idx += i
                break

            if now[idx-i] != name[idx-i]:
                c += i; 
                if idx-i > 0:
                    idx -= i
                else:
                    idx = len(name) + idx - i
                break
                     
    return c

nn = "AABAAAAAAABBB"
print(solution(nn))
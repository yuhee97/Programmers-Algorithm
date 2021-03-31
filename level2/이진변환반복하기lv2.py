def check(ss):
    n0 = 0; n1 = 0
    for i in range(len(ss)):
        if ss[i] == '1':
            n1+=1
        else:
            n0+=1
    return n1, n0

def binary(cc):
    st = ''
    if cc == 1:
        return '1'
    while True:
        r = cc % 2
        cc = cc // 2
        st = str(r) + st
        if cc == 0:
            break
    return st
        
def solution(s):
    n = 0; c = 0
    while s != '1':
        change, num = check(s)
        n += num
        c += 1
        s = binary(change)
        if s == '1':
            return [c, n]
    return [0, 0]

s = "110010101001"
print(solution(s))
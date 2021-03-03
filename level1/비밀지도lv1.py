def solution(n, arr1, arr2):
    n1 = []; n2 = []; result = []
    for i in range(n):
        a1 = arr1[i]; str_a1 = ''
        while a1 > 0:
            r = a1 % 2
            a1 = a1 // 2
            str_a1 = str(r) + str_a1
        if len(str_a1) < n:
            str_a1 = '0'*(n-len(str_a1)) + str_a1
        n1.append(list(str_a1))   

        a2 = arr2[i]; str_a2 = ''
        while a2 > 0:
            r = a2 % 2
            a2 = a2 // 2
            str_a2 = str(r) + str_a2
        if len(str_a2) < n:
            str_a2 = '0'*(n-len(str_a2)) + str_a2
        n2.append(list(str_a2))  

    for i in range(n):
        strr = ''
        for j in range(n):
            if n1[i][j] == '1' or n2[i][j] == '1':
                strr += '#'
            else:
                strr += ' '
        result.append(strr)

    return result

nn = 5
arr_1 = [9, 20, 28, 18, 11]
arr_2 = [30, 1, 21, 17, 28]

print(solution(nn, arr_1, arr_2))
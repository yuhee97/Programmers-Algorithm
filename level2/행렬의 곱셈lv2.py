def solution(arr1, arr2):

    rep1 = len(arr1); rep2 = len(arr2[0])
    result = [[0] * rep2 for _ in range(rep1)]

    for i in range(rep1):
        for j in range(rep2):
            for k in range(len(arr1[0])):
                result[i][j] += (arr1[i][k] * arr2[k][j])

    return result

ar1 = [[1, 4], [3, 2], [4, 1]]
ar2 = [[3, 3], [3, 3]]
print(solution(ar1, ar2))

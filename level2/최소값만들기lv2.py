def solution(A,B):
    A.sort(); SUM = 0
    B.sort(reverse = True)
    for i in range(len(A)):
        SUM += A[i] * B[i]
    return SUM

a = [1,2,3,5]
b = [6,7,4,2]
print(solution(a, b))
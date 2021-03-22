def solution(number, k):
    stack = []; n = len(number)
    stack.append(number[0])
    for i in range(1, n):
        num = number[i]
        while k > 0 and len(stack) > 0 and stack[-1] < num:
            stack.pop()
            k-=1
        stack.append(num)

    if k > 0:
        return ''.join(stack[0:n-k])
    else:
        return ''.join(stack)

number = "1234525342534"
k = 4
print(solution(number, k))
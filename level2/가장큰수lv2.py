def solution(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers = sorted(str_numbers, reverse=True, key=lambda x: x*3)
    return str(int(''.join(str_numbers)))

n = [6, 10, 2]
print(solution(n))
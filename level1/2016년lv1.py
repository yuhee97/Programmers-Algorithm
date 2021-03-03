def solution(a, b):
    month_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    n = 0; day = ['FRI', 'SAT', 'SUN','MON','TUE','WED','THU']
    for i in range(a-1):
        n += month_day[i]
    n += b
    return day[n%7-1]

a_ = 5
b_ = 24
print(solution(a_, b_))

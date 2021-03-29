def solution(numbers, hand):
    r = '#'; l = '*'; n = len(numbers)
    l_n = [1, 4, 7] 
    r_n = [3, 6, 9]
    table = [['1', '2', '3'], ['4', '5', '6'], 
             ['7', '8', '9'], ['*', '0', '#']]
    result = ''
    for i in range(n):
        if numbers[i] in l_n:
            result += 'L'
            l = str(numbers[i])
        elif numbers[i] in r_n:
            result += 'R'
            r = str(numbers[i])
        else:
            for h in range(4):
                for w in range(3):
                    if table[h][w] == str(numbers[i]):
                        x = h; y = w
                    if table[h][w] == r:
                        r_x = h; r_y = w
                    if table[h][w] == l:
                        l_x = h; l_y = w
            if abs(l_x-x)+abs(l_y-y) > abs(r_x-x)+abs(r_y-y):
                result += 'R'
                r = str(numbers[i])
            elif abs(l_x-x)+abs(l_y-y) == abs(r_x-x)+abs(r_y-y):
                result += hand[0].upper()
                if hand[0].upper() == 'R':
                    r = str(numbers[i])
                else:
                    l = str(numbers[i])
            else:
                result += 'L'     
                l = str(numbers[i])

    return result

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))
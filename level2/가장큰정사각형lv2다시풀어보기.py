def solution(board):
    answer = 0
    for m in range(0,len(board)):
        for n in range(0,len(board[0])):
            if m == 0 or n == 0:
                if board[m][n] == 1 and answer == 0:
                    answer = 1
                continue
            if board[m][n] == 1:
                board[m][n] = min(board[m-1][n], board[m-1][n-1], board[m][n-1]) + 1
                if board[m][n] > answer:
                    answer = board[m][n]
    return answer ** 2

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]	
print(solution(board))
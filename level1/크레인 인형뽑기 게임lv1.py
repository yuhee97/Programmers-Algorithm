def solution(board, moves):
    
    idx = len(board)
    boxes = [[] for _ in range(idx)]
    n_board = []
    
    for i in range(idx):
        for j in range(idx):
            if board[i][j] != 0:
                boxes[j].append(board[i][j])
    c = 0
    
    for m in moves:
        if boxes[m-1]:
            n_board.append(boxes[m-1].pop(0))
            if len(n_board) > 1 and n_board[-1] == n_board[-2]:
                print(n_board)  
                n_board.pop(); n_board.pop()
                c += 2           
    return c
            
b = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
m = [1,5,3,5,1,2,1,4]
print(solution(b, m))
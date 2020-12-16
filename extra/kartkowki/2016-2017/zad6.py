def solve(board):
    sy = [sum(row) for row in board]
    sx = [0]*len(board)

    for x in range(len(board)):
        for y in range(len(board)):
            sx[x] += board[y][x]

    print(sx)
    print(sy)
    
    best_s = 0
    best_pos1 = ()
    best_pos2 = ()

    for x1 in range(len(board)):
        for y1 in range(len(board)):
            for x2 in range(len(board)):
                for y2 in range(len(board)):

                    if x1 == x2 and y1 == y2:
                        continue
                    
                    norm = 0
                    if x1 != x2 and y1 != y2:

                        s1 = sx[x1] + sy[y1] - board[y1][x1]
                        s2 = sx[x2] + sy[y2] - board[y2][x2]
                        norm = -board[y2][x1] - board[y1][x2]
                        
                    elif x1 == x2:
                        s1 = sx[x1] + sy[y1]
                        s2 = sy[y2]

                    elif y1 == y2:
                        s1 = sx[x1] + sy[y1]
                        s2 = sx[x2]
                        
                    if s1 + s2 + norm> best_s:
                        print(s1, s2)
                        print(x1,y1,x2,y2)
                        best_pos1 = (x1, y1)
                        best_pos2 = (x2, y2)
                        best_s = s1+s2 + norm
                        print(best_s)
                    
    return best_pos1, best_pos2



board = [
    [3,1,4,7,3],
    [3,1,6,7,1],
    [3,1,12,7,1],
    [3,1,4,7,8],
    [3,1,4,7,3],
] 

print(solve(board))
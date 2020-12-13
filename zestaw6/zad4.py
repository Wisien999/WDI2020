moves = ((1, 2), (-1, 2), (1, -2), (-1, -2),
         (2, 1), (2, -1), (-2, 1), (-2, -1))


def rek(board, x=0, y=0, i=0):
    if board[y][x] == -1:
        board[y][x] = i
    else:
        return i-1

    for x_m, y_m in moves:
        try:
            i = rek(board, x+x_m, y+y_m, i+1)
        except IndexError:
            pass
    
    return i



n = 5
board = [[-1]*n for _ in range(n)]
print(rek(board))



def t_print(t):
    for i in range(len(t)):
        for j in range(len(t)):
            print(t[i][j], end='\t')
        print('')
    print()


t_print(board)
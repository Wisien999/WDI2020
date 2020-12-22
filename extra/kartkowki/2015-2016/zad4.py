# 2) Dana jest tablica t[N][N] (reprezentująca szachownicę) wypełniona liczbami całkowitymi z zakresu -9 ..9. Proszę napisać funkcję.która
# ustawia na szachownicy dwie wieŹe, tak aby suma liczb na szachowanych polach była największa. Do funkcji należy przekazać tablicę, funkcja
# powinna zwrócić położenie wież'
# Uwaga:
# - Zakładamy, że pole na którym stoi wieża jest przez nią szachowane.
import math



def solve(board):
    n = len(board)

    def suma(x1, y1, x2, y2):
        if x1 != x2 and y1 != y2:
            return s_x[x1] + s_y[y1] + s_x[x2] + s_y[y2] - board[y1][x2] - board[y2][x1] - board[y1][x1] - board[y2][x2]
        if x1 == x2 and y1 != y2:
            return s_x[x1] + s_y[y1] + s_y[y2] - board[y1][x1] - board[y2][x2]
        if x1 != x2 and y1 == y2:
            return s_x[x1] + s_x[x2] + s_y[y2] - board[y1][x1] - board[y2][x2]



    def s_k_c(board):

        s_x = [0]*n
        s_y = [0]*n

        for i in range(n**2):
            x = i % len(board)
            y = i // len(board)
            s_x[x] += board[y][x] 
            s_y[y] += board[y][x]

        # print(s_x)
        # print(s_y)

        return s_x, s_y


    s_x, s_y = s_k_c(board)

    best = -math.inf

    for i1 in range(n**2):
        x1 = i1 % n
        y1 = i1 // n
        for i2 in range(n):
            x2 = i2 % n
            y2 = i2 // n

            if x1 == x2 and y1 == y2:
                continue
            
            s = suma(x1, y1, x2, y2)

            if s > best:
                best = s
                
                best_1 = (x1, y1)
                best_2 = (x2, y2)

                # print("new best", best)
                # print(best_1, best_2)


    return best, best_1, best_2


def print_board(board):
    for row in board:
        for el in row:
            print(el, end="\t")
        print()
    
    print()


board = [
    [-8,-2,6,4,7,3,7],
    [-8,-2,6,4,7,3,7],
    [6,-2,6,4,7,3,7],
    [-8,-2,6,4,7,-9,7],
    [-8,-2,6,7,7,3,7],
    [2,2,-6,4,7,3,7],
    [-8,-2,6,4,7,3,7],
]

board = [
    [1, 7, 9, 9, -1, 4, -5],
    [-5, -8, -9, -3, 1, -3, 6],
    [-8, 7, -7, 8, 0, 3, -5],
    [4, 9, 9, 2, 2, 1, -7],
    [-9, 9, 6, -7, -3, -4, 5],
    [6, 1, -4, -1, -2, 5, -1],
    [-2, 6, -6, -1, -8, 2, 6],
]

print_board(board)

print(solve(board))
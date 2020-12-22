def checked_sum(board, w, ignore = None):
    ignore = ignore or []

    n = len(board)

    checked_s = 0
    checked = [[False]*n for _ in range(n)]

    for x in range(len(w)):
        if x in ignore:
            continue

        y = w[x]

        for i in range(n):
            if i != x:
                checked[y][i] = True

        for i in range(n):
            if i != y:
                checked[i][x] = True
        
    
    for x in range(len(board)):
        for y in range(len(board)):
            if checked[y][x]:
                checked_s += board[y][x]
    
    return checked_s


def solve(board, w):
    best_s = checked_sum(board, w)
    best_x1 = 0
    best_x2 = 0

    for x1 in range(len(w)):

        for x2 in range(len(w)):
            if x1 == x2:
                continue

            s = checked_sum(board, w, [x1, x2]) 
            if s < best_s:
                best_x1 = x1
                best_x2 = x2
                best_s = s

    return best_s, best_x1, best_x2



def print_board(board):
    for row in board:
        for el in row:
            print(el, end="\t")
        print()
    
    print()


board = [
    [4,8,32,534,1,4,-123,4],
    [4,8,32,534,-1,4,-123,4],
    [4,89,2,534,-1,-4,-123,4],
    [4,8,32,534,-1,4,-123,-4],
    [0,8,3,5-34,1,4,-12-3,4],
    [4,8,32,-5-3-4,1,4,-123,4],
    [11,8,32,53-4,1,4,-123,4],
    [4,-8,32,534,-1,-4,-123,4],
]

w = [1,5,3,4,5,6,7,2]


print_board(board)
print(checked_sum(board, w))

print(solve(board, w))
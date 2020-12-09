def rek(board, safe, y=0, s=0, h = []):
    if y == len(board):
        # print("-------------------")
        # print_tab(safe)
        print(h)
        # print("-------------------")

        return s == 0

    moves = {1, 0,-1}
    # moves = [(1, 1), (1,0), (1,-1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (0, 0), (0, 1)]


    for x in range(len(board[y])):
        if not safe[y][x]:
            continue

        for m_x in moves:
            try:
                safe[y+1][x+m_x] = False
            except IndexError:
                pass
        
        # print("-------------------")
        # print("czesssssss")
        # print_tab(safe)
        # print("-------------------")

        if rek(board, safe, y+1, s+board[y][x], [*h, board[y][x]]):
            return True


        for m_x in moves:
            try:
                safe[y+1][x+m_x] = True
            except IndexError:
                pass
    
    return False
        
def safeTab(dim):
    return [[True]*dim for _ in range(dim)]

def print_tab(tab):
    for r in tab:
        print(r)


board = [
    [4,6,3,7,1],
    [4,6,3,7,3],
    [4,-6,3,7,1],
    [4,6,-3,7,-3],
    [4,6,3,7,1]
]

print(rek(board, safeTab(len(board))))
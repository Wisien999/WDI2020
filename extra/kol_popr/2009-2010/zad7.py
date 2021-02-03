def nwd(a, b):
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a%b
    
    return a



def solve(tab):
    moves = [(2,1), (-2,1), (1,2), (-1,2)]

    for y in range(len(tab)):
        for x in range(len(tab)):
            for x_m, y_m in moves:
                if x+x_m >=0 and x+x_m < len(tab) and y+y_m >= 0 and y+y_m < len(tab):
                    nx = x+x_m
                    ny = y+y_m
                    if nwd(tab[ny][nx], tab[y][x]) == 1:
                        print(x,y)
                        return True
    
    return False



board = [
    [8,4,6,12,2],
    [8,4,6,12,2],
    [8,8,6,12,2],
    [8,4,3,12,2],
    [8,4,6,12,2]
]

print(solve(board))



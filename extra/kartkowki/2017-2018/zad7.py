
def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    for i in range(6, int(num**0.5) + 2, 6):
        if num % (i-1) == 0 or num % (i+1) == 0:
            return False

    return True


def check(t, x, y):
    moves = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]

    for x_m, y_m in moves:
        if x+x_m < 0 or y+y_m < 0 or x+x_m >= len(t) or y+y_m >= len(t):
            continue
        
        if is_prime(t[y][x] + t[y+y_m][x+x_m]):
            return True
    
    return False


def find(t): # main driver
    for x in range(len(t)):
        for y in range(len(t)):
            if check(t, x, y):
                return True
    
    return False



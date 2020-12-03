def convert2rd(x, y):
    return x + y//2


def convert2ld(x, y):

    # return x + y//2 - 1

    if x > y:
        ldx = x - y
        ldy = 0
    else:
        ldx = 0
        ldy = y - x

    return ldx + 7 - ldy



def rek(n, left, x_tab, y_tab, ld_tab, rd_tab, history=[]):
    if left == 0:
        global pos
        pos = history
        return True

    
    for x in range(n):
        for y in range(n):
            if not x_tab[x] and not y_tab[y] and not ld_tab[convert2ld(x, y)] and not rd_tab[convert2rd(x, y)]:
                x_tab_c = x_tab.copy()
                y_tab_c = y_tab.copy()
                ld_tab_c = ld_tab.copy()
                rd_tab_c = rd_tab.copy()

                x_tab_c[x] = True
                y_tab_c[y] = True
                ld_tab_c[convert2ld(x, y)] = True
                rd_tab_c[convert2rd(x, y)] = True

                if rek(n, left-1, x_tab_c, y_tab_c, ld_tab_c, rd_tab_c, [*history, (x,y)]):
                    return True
                
    return False

pos = []

n=8
rek(n, 8, [False]*n, [False]*n, [False]*(2*n-1), [False]*(2*n-1), [])
print(pos)

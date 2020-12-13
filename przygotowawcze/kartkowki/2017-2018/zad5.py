# Zadanie 1.
# Dana jest tablica t[N][N] (reprezentuj¡ca szachownic¦) wypeaniona liczbami naturalnymi. Na szachownicy
# znajduj¡ si¦ dwie wie»e. Prosz¦ napisa¢ funkcj¦, która odpowiada na pytanie: czy istnieje ruch wie»¡
# zwi¦kszaj¡cy sum¦ liczb na "szachowanych" przez wie»e polach? Do funkcji nale»y przekaza¢ tablic¦ oraz
# poao»enia dwóch wie», funkcja powinna zwróci¢ warto±¢ logiczn¡.
# Uwaga: zakaadamy, »e wie»a szachuje caay wiersz i kolumn¦ z wya¡czeniem pola, na którym stoi.


def check(t, pos):
    x1, y1 = pos[0]
    x2, y2 = pos[1]
    
    # s = sum(t[y1]) + sum(t[y2]) + sum(t[i][x1] for i in range(len(t))) + sum(t[i][x2] for i in range(len(t))) #- t[y1][x1] - t[y2][x2]
    sum_row = [sum(row) for row in t]
    sum_col = [sum(t[i][j] for i in range(len(t))) for j in range(len(t))]
    s = sum_col[x1] + sum_col[x2] + sum_row[y1] + sum_row[y2] - t[y1][x1] - t[y2][x2]

    x = len(t)
    while x > 0:
        x -= 1
        if x != x1 and x != x2 and sum_col[x] + sum_row[y1] + sum_col[x2] + sum_row[y2] - t[y1][x] - t[y2][x2] > s:
            return True

    y = len(t)
    while y > 0:
        y -= 1
        if y != y1 and y != y2 and sum_col[x1] + sum_row[y] + sum_col[x2] + sum_row[y2] - t[y][x1] - t[y2][x2] > s:
            return True

    x = len(t)
    while x > 0:
        x -= 1
        if x != x1 and x != x2 and sum_col[x1] + sum_row[y1] + sum_col[x] + sum_row[y2] - t[y1][x1] - t[y2][x] > s:
            return True
    
    y = len(t)
    while y > 0:
        y -= 1
        if y != y1 and y != y2 and sum_col[x1] + sum_row[y1] + sum_col[x2] + sum_row[y] - t[y1][x1] - t[y][x2] > s:
            return True

    return False



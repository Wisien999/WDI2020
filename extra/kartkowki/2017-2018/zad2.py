# Zadanie 2
# const int N=1000;
# int tab[N];
# Tablica tab jest wypeaniona liczbami naturalnymi. Prosz¦ napisa¢ funkcj¦, która zwraca daugo±¢ najdau»szego
# spójnego podci¡gu rosn¡cego, dla którego suma jego elementów jest równa sumie indeksów tych elementów.
# Do funkcji nale»y przekaza¢ tablic¦, funkcja powinna zwróci¢ daugo±¢ znalezionego podci¡gu, lub warto±¢ 0,
# je»eli taki podci¡g nie istnieje.

def check(tab):
    best_leng = 1
    curr_leng = 1
    for i in range(1, len(tab)):
        if tab[i-1] >= tab[i]:
            best_leng = max(best_leng, curr_leng)
        else:
            curr_leng += 1
    
    return max(best_leng, curr_leng)

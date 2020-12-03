# Bartłomiej Wiśniewski
# Najważniejsza jest długość ciągu. Liczba binarna o większej długości zawsze będzie większa od liczby binarnej o mniejszej długości.
# Żeby znaleźć największą liczbę wystarczy wybrać liczby gdzie pierwsza 1 jest najwcześniej. Następnie szukać drugiej 1 w tych liczbach itp.
# analogicznie dla najmniejszej liczby


def distance(T):
    first_first1 = len(T)
    last_first1 = 0
    mini_f = 0
    maxi_l = len(T)
    pos1 = 0
    pos2 = 0

    counter_f = 2
    counter_l = 2
    while counter_f > 1 and counter_l > 1:
        for row in T:
            i = mini_f
            while i < len(row) and row[i] == 0:
                i += 1
            
            if first_first1 > i and mini_f <= i:
                first_first1 = i
                pos1 = i
                counter_f = 1
            elif first_first1 == i and mini_f <= i:
                counter_f += 1
            
            if last_first1 < i and maxi_l >= i:
                last_first1 = i
                pos2 = i
                counter_l = 1
            elif last_first1 == i and maxi_l >= i:
                counter_l += 1
        
        mini_f = first_first1+1
    
    return abs(pos1-pos2)


#end def

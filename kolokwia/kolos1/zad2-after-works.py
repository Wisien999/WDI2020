# Bartłomiej Wiśniewski
# Najważniejsza jest długość ciągu. Liczba binarna o większej długości zawsze będzie większa od liczby binarnej o mniejszej długości.
# Żeby znaleźć największą liczbę wystarczy wybrać liczby gdzie pierwsza 1 jest najwcześniej. Następnie szukać drugiej 1 w tych liczbach itp.
# analogicznie dla najmniejszej liczby


def distance(T):
    pos_smallest = 0
    pos_greatest = 0
    smallest = T[0]
    greatest = T[0]

    for pos, row in enumerate(T):
        i = 0
        while i < len(row) and row[i] == smallest[i]:
            i += 1
        
        if i < len(row) and row[i] == 0:
            smallest = row
            pos_smallest = pos
    

    for pos, row in enumerate(T):
        i = 0
        while i < len(row) and row[i] == greatest[i]:
            i += 1
        
        if i < len(row) and row[i] == 1:
            greatest = row
            pos_greatest = pos
    
    return abs(pos_greatest - pos_smallest)

#end def


print(distance([
[1,0,0,0,1,1,1,0],
[1,0,1,0,1,1,1,0],
[0,0,0,0,1,1,1,0],
[0,0,0,0,1,0,1,0],
[1,0,0,0,1,1,1,1],
[1,1,0,1,1,0,1,0],
[1,0,0,0,0,0,1,0],
[1,1,1,0,1,1,1,1]
]))
# Reszta
# Proszę napisać funkcję, która dla podanej sumy i listy
# nominałów wypisuje ilość możliwości na jakie możliwości
# na jakie można wydać daną sumę.


def reszty(nominaly, i=0, cs=0):
    if cs == 0:
        return 1

    if i == len(nominaly):
        return 0

    if cs < 0:
        return 0

    if cs >= nominaly[i]:
        return reszty(nominaly, i, cs-nominaly[i]) + reszty(nominaly, i+1, cs)

    return reszty(nominaly, i+1,cs)

    


arr = [1,2,5]
print(reszty(arr, cs=5))


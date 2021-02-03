def solve(t1,t2):
    i1,i2 = 0,0

    deleted = [-1]*len(t1)
    p = 0

    while i1 < len(t1) and i2 < len(t2):
        if t1[i1] > t2[i2]:
            i2 += 1
        elif t1[i1] < t2[i2]:
            i1 += 1
        else:
            deleted[p] = t1[i1]
            p += 1
            del t1[i1]
            del t2[i2]

    return [el for el in deleted if el != -1]


a1 = [1,5,7,8,10]
a2 = [1,3,8,9,10]
print(solve(a1, a2))
print(a1, a2)
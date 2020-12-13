def solve(t):
    bstart, bstop = 0, 0
    counter = 0
    start = 0
    for i in range(1, len(t)):
        if t[i] != t[i-1]:
            if i-start > bstop - bstart:
                bstart = start
                bstop = i
            elif i-start == bstop - bstart:
                counter += 1
        
            start = i
        
    if len(t)-start > bstop - bstart:
        bstart = start
        bstop = i
    elif len(t)-start == bstop - bstart:
        counter += 1

    # print(counter)
    if counter > 0:
        return 0

    return bstop - bstart, [t[i] for i in range(len(t)) if i < bstart or i >= bstop]


arr = [3,3,3,3,3,3,5,7,11,13,13,1,2,2,2,2,2,2]
# arr = [1,3,3,3,3,5,7,11,13,13,1,2,2,2,2,3]

print(solve(arr))
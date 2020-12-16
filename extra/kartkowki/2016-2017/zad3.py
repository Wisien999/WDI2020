def get_kth_c(k):
    a1, a2 = 1, 1
    b1, b2, b3 = 1, 1, 1
    c = 1

    i = 1
    while i < k:
        # print(c, a2, b3)
        if c >= a2:
            a1, a2 = a2, a1+a2
        if c >= b3:
            b1, b2, b3 = b2, b3, b1+b2+b3
        
        mini = min(b3, a2)
        # maxi = max(b3, a2)

        if c <= mini:
            c = mini
            i += 1
    
    return c



print(get_kth_c(int(input())))
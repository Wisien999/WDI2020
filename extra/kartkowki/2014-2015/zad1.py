def solve(tab, k):
    def insert(tab, n, val):
        if n == 0:
            tab[0] = val
            return 1

        p, q = 0, n
        while p < q:
            r = (p+q)//2
            if tab[r] > val:
                q = r
            elif tab[r] < val:
                p = r+1
            else:
                break

        r += 1
        # return r
        # print(r)
        for i in range(n-1, r-1, -1):
            tab[i+1] = tab[i]
        
        tab[r] = val
    
        return leng+1
    



    helper = [0]*(k+2)
    leng = 0
    for elem in tab:
        print(leng)
        if leng > k-1:
            
            for i in range(leng-1, -1, -1):
                helper[i+1] = tab[i]
            
            helper[leng] = 0
            leng -= 1

        leng = insert(helper, leng, elem)
        # leng += 1

    return helper


# arr = [5,2,7,5,2,4,7]
# print(solve(arr, 5))




arr = [2,5,7,7,9,12,34,76, 0]

print(arr)


arr = [5,734,32,6,3,68,4]

print(solve(arr, 5))
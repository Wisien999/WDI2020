def solve(t1, t2):

    best = 0

    # def rek(t1, t2, i=0, s1=0, s2=0, leng1=0, leng2=0, h=None):
    def rek(t1, t2, i=0, s1=0, s2=0, leng1=0, leng2=0):
        if i == len(t1):
            if s1 == s2 and leng1 == leng2:
                nonlocal best
                # best = max(best, leng1)
                if best < leng1:
                    best = leng1
                    # print("git", h)
            return

            
        # # print("ccc")
        # rek(t1, t2, i+1, s1, s2, leng1, leng2, [*h])
        # rek(t1, t2, i+1, s1, s2+t2[i], leng1, leng2+1, [*h, (i, "t2")])
        # rek(t1, t2, i+1, s1+t1[i], s2+t2[i], leng1+1, leng2+1, [*h, (i,"oba")])
        # rek(t1, t2, i+1, s1+t1[i], s2, leng1+1, leng2, [*h, (i, "t1")])
            
        # print("ccc")
        rek(t1, t2, i+1, s1, s2, leng1, leng2)
        rek(t1, t2, i+1, s1, s2+t2[i], leng1, leng2+1)
        rek(t1, t2, i+1, s1+t1[i], s2+t2[i], leng1+1, leng2+1)
        rek(t1, t2, i+1, s1+t1[i], s2, leng1+1, leng2)


    rek(t1, t2, 0, 0, 0, 0, 0)

    return best
    

arr1 = [1,1,2,3,1]
arr2 = [2,1,1,1,1]
print(solve(arr1, arr2))
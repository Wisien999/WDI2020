def solve(x, y, n):
    def opA(num):
        return num+3

    def opB(num):
        return num*2

    def opC(num):
        res = 0
        power = 1

        while num > 0:
            d = num%10
            num //= 10
            if d%2 == 0:
                d += 1
            
            res += d*power
            power *= 10
        
        return res


    # print(opC(2356))

    def rek(num, target, n, last, no_pos, h):
        if num == target:
            print(h)
            return no_pos+1
        
        if n == 0:
            return no_pos
        

        if last != "A":
            no_pos = rek(opA(num), target, n-1, "A", no_pos, h+["A"])
            # print("level", len(h), "a", no_pos)

        if last != "B":
            no_pos = rek(opB(num), target, n-1, "B", no_pos, h+["B"])
            # print("level", len(h), "a", no_pos)

        if last != "C":
            no_pos = rek(opC(num), target, n-1, "C", no_pos, h+["C"])
            # print("level", len(h), "a", no_pos)
        
        return no_pos

    return rek(x,y,n, "", 0, [])


print(solve(2356,3360,3))
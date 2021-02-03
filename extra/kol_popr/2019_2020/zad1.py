def ex1(arr):
    candidates = set()

    def gcd(a, b):
        while b != 0:
            a, b = b, a%b
        
        return a

    for y in range(len(arr)):
        for x in range(len(arr)):
            ans = float("inf")
            if x >= 1:
                ans = gcd(arr[y][x-1], arr[y][x])
                if ans == 1:
                    candidates.add((x, y, x-1, y))
            if x < len(arr)-1:
                ans = gcd(arr[y][x+1], arr[y][x])
                if ans == 1:
                    candidates.add((x, y, x+1, y))
            if y >= 1:
                ans = gcd(arr[y-1][x], arr[y][x])
                if ans == 1:
                    candidates.add((x, y, x, y-1))
            if y < len(arr)-1:
                ans = gcd(arr[y+1][x], arr[y][x])
                if ans == 1:
                    candidates.add((x, y, x, y+1))

    
    for cand1 in candidates:
        for cand2 in candidates:
            if cand1 == cand2:
                continue
                
            if cand1[0] == cand2[0] or cand1[0] == cand2[2] or cand1[1] == cand2[1] or cand1[1] == cand2[3]:
                continue
        
            if cand1[0] == cand1[2] and cand2[1] == cand2[3] or cand1[1] == cand1[3] and cand2[0] == cand2[2]:
                nwd1 = gcd(arr[cand1[0]][cand1[1]], arr[cand1[2]][cand1[3]])
                nwd2 = gcd(arr[cand2[0]][cand2[1]], arr[cand2[2]][cand2[3]])

                nwd = gcd(nwd1, nwd2)

                return nwd == 1

    return False

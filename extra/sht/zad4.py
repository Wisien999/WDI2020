def solve(t, s):
    seen = dict()

    for i, el in enumerate(t):
        if s-el in seen:
            return seen.get(s-el), i
        
        seen[el] = i
    
    return False


print(solve([8,7,2,5,3,1], 10))
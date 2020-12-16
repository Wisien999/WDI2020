import math


def check(t, num_mask):
    s_g = 0
    d = num_mask%2
    
    i = 0
    while num_mask % 2 == d:
        # print(i, s_g, num_mask)
        s_g += t[i]
        num_mask //= 2
        i += 1

    # print(s_g)
    # s2 = 0
    while num_mask > 0:
        s2 = 0
        d = num_mask%2
        while num_mask > 0 and num_mask % 2 == d:
            s2 += t[i]
            num_mask //= 2
            i += 1
            # print(i, num_mask, s2, s_g)

            if i == len(t):
                return s2 == s_g
        
        if s2 != s_g:
            return False
        
        # s2 = 0
    
    return True




def parts(num_mask, leng):
    
    counter = 1
    if int(math.log2(num_mask))+1 < leng:
        # print("aaaa")
        counter += 1

    l = num_mask % 2
    while num_mask > 0:
        if num_mask%2 != l:
            counter += 1
            l = num_mask%2

        num_mask //= 2

    return counter


# print(parts(5, 3))
# print(parts(4, 3))
# print(parts(3, 3))
# print(parts(1, 3))

# def parts(m, n):
#     mas = [0]*n
    

#     for i in range(n):
#         mas[i] = m%2
#         m //= 2
        
#     counter = 1
#     last = mas[0]
#     for i in range(n):
#         if last != mas[i]:
#             counter += 1
#             last = mas[i]
    
#     return counter


def solve(t):
    best = 0
    for mask in range(1, 2**(len(t)-1)+1):
        if check(t, mask):
            best = max(best, parts(mask, len(t)))
    
    return best


print(solve([1,2,3,1,5,2,2,2,6]))
    
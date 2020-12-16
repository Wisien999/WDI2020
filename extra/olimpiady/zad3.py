def square_root(num, digits):
    limit = 10**(digits+2)
    a = 5 * num
    b = 5
    while b < limit:
        if a >= b:
            a -= b
            b += 10
        else:
            a *= 100
            b = (b//10)*100 + 5
    
    return b // 100


print(sum(map(int, str(square_root(26, 5))[1:])))
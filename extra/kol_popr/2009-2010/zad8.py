def rek(zeros, ones, h, counter):
    if zeros < 0 or ones < 0:
        return counter

    if zeros == 0 and ones == 0:
        num = to_dec(h)
        if num > 1 and not is_prime(num):
            return counter+1
        
        return counter
    

    counter = rek(zeros-1, ones, [*h, 0], counter)
    counter = rek(zeros, ones-1, [*h, 1], counter)

    return counter


def to_dec(arr):
    num = 0
    power = 1

    for i in arr[::-1]:
        num += i*power
        power *= 2
    

    return num




def is_prime(num):
    if num <= 1:
        return False
    
    if num == 2 or num == 3:
        return True
    
    if num%2==0 or num%3 == 0:
        return False
    

    for i in range(6, int(num**0.5)+3, 6):
        if num % (i-1) == 0 or num % (i+1) == 0:
            return False
    
    return True



def solve(ones, zeros):
    return rek(zeros, ones-1, [1], 0)



print(solve(2,3))
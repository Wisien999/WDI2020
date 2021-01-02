def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num%2 == 0 or num %3 == 0:
        return False
    
    for i in range(6, int(num**0.5)+3, 6):
        if num % (i-1) == 0 or num % (i+1) == 0:
            return False
    
    return True

def solve(tab):
    f1, f2 = 1, 1
    prime = False

    for i in range(len(tab)):
        if i == f2:
            f1, f2 = f2, f1+f2

            if tab[i] <= 1 or is_prime(tab[i]):
                return False
        else:
            if not prime:
                prime = is_prime(tab[i])
    
    return prime


arr = [2,42,42,42,11,12,54,6,56,24,2,3]
print(solve(arr))
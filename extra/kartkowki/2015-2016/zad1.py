primes = (2, 3, 5, 7, 11, 13)

def check(num, base):

    while num > 0:
        if num % base not in primes:
            return False
        num //= base
    
    return True


def ex(num):
    # systemu 2 nie ma sensu sprawdzać
    for base in range(3, 17):
        if check(num, base):
            return True, base
    
    return False


print(ex(int(input())))
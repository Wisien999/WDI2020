t = [0]*9
t[0] = 1

primes = {2,3,5,7}

def test(i = 1):
    if i == len(t):
        print(t)
        return

    for num in range(1, 10):
        if abs(t[i-1] - num) >= 2:
            if num in primes and t[i-1] in primes:
                continue

            t[i] = num
            test(i+1)

test()
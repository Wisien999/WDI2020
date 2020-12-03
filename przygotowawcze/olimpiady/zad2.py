import math


primes = []

def simple_sieve(limit):
    mark = [True for i in range(limit + 1)]
    p = 2
    while (p * p <= limit):
		
		# If p is not changed, then it is a prime 
        if (mark[p] == True): 
			
			# Update all multiples of p 
            for i in range(p * p, limit + 1, p): 
                mark[i] = False
        p += 1
		
	# Print all prime numbers 
	# and store them in prime 
    for p in range(2, limit): 
        if mark[p]:
            primes.append(p)

            # print(primes)
    

def segmented_sieve(n):
    n = int(n)
    limit = int(math.floor(math.sqrt(n)) + 1)
    simple_sieve(limit)

    low = limit
    high = limit*2 

    while low < n:
        if high >= n:
            high = n
        
        mark = [True for _ in range(limit+1)]
        
        for prime in primes:
            
            loLim = int(math.floor(low/prime)*prime)
            if loLim < low:
                loLim += prime
            
            
            for p in range(loLim, high, prime):
                mark[p-low] = False
        
        for candidate in range(low, high):
            if mark[candidate-low]:
                primes.append(candidate)
        
        low += limit
        high += limit
    


# segmented_sieve(1000)
# print(primes)
# print(len(primes))


def is_palindrome(num):
    num = str(num)
    return num == num[::-1]


print(is_palindrome(100111))
print(is_palindrome(1001))

n = 100
# n = int(input())


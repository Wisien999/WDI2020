def solve(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2 or num == 3:
            return True
        if num%2 == 0 or num%3 == 0:
            return False
        
        for i in range(6, int(num**0.5)+2):
            if num % (i+1) == 0 or num % (i-1) == 0:
                return False
        
        return True



    def reverse_num(num):
        ans = 0
        while num > 0:
            ans *= 10
            ans += num % 10
            num //= 10
        

        return ans


    def rek(n, n1, n2, i): 
        
        if n == 0:
            n1 = reverse_num(n1)
            n2 = reverse_num(n2)
            if is_prime(n1) and is_prime(n2):
                print(n1, n2)
                return i+1
            return i
            



        i = rek(n//10, (n1*10)+(n%10), n2, i)
        
        i = rek(n//10, n1, (n2*10)+(n%10), i)

        return i



    return rek(n, 0, 0, 0)


print(solve(525433))
print("------------------")
print(solve(21523))
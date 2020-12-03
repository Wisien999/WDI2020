n = int(input())

factorial = 1
for i in range(2, n+1):
    factorial *= i
    while factorial % 10 == 0:
        factorial //= 10

print(factorial % 10)

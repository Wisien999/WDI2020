n = int(input())

no_of_5 = 0
power = 5
while power <= n:
    no_of_5 += n//power
    power *= 5

skip = no_of_5
# print(no_of_5)

last_digit = 1
for i in range(1, n+1):
    # print(i)
    while i % 5 == 0:
        i //= 5
    if skip > 0 and i%2 == 0:
        i //= 2
        skip -= 1
    # print(i)
    last_digit = (last_digit * i)%10


print(last_digit)
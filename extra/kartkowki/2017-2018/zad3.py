def can_be_summed(num):
    f1, f2 = 1, 1
    fib_suma = 0
    while fib_suma < num:
        fib_suma += f1
        f1, f2 = f2, f1+f2


    f1, f2 = 1, 1
    while fib_suma > num:
        fib_suma -= f1
        f1, f2 = f2, f1+f2


    return fib_suma == num


def find(num):
    num += 1

    while can_be_summed(num):
        num += 1

    print(num)

find(4)
find(10)
find(15)
find(18)
find(22)
find(23)
# Bartłomiej Wiśniewski
# Rekurencyjnie dzielę liczbę na kawałki, Na każdym "indeksie" liczby podejmuję decyzję czy rozpocząć nowy podział czy nie.

import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num%2 == 0 or num%3 == 0:
        return False
    
    for i in range(6, int(num**0.5)+3, 6):
        if num % (i+1) == 0 or num % (i-1) == 0:
            return False
    
    return True


# from time import sleep

def rek(num, nums, i, parts):
    # print(num, nums, i, parts)
    # sleep(0.2)

    if is_prime(num) and is_prime(parts):
        return True

    if i > num:
        return False
    

    if is_prime(num%i):
        if rek(num//i, [num%i] + nums, 10, parts+1):
            return True
    

    return rek(num, [*nums], i*10, parts)


def divide(N):
    return rek(N, [], 10, 1)


class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


print(Color.RED + Color.BOLD + str(divide(273)) + Color.END) # True, podział 2|7|3
print(Color.RED + Color.BOLD + str(divide(22222)) + Color.END) # True, podział 2|2|2|2|2
print(Color.RED + Color.BOLD + str(divide(23672)) + Color.END) # True, podział 23|67|2
print(Color.RED + Color.BOLD + str(divide(2222)) + Color.END) # False
print(Color.RED + Color.BOLD + str(divide(21722)) + Color.END) # False

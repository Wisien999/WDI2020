# Bartłomiej Wiśniewski

def to_base(num, base):
    arr = [0]*num
    i = num-1

    num_c = num
    while num_c > 0:
        arr[i] = num_c % base
        num_c //= base
        i -= 1
    #end while

    for i in range(num):
        arr[i], arr[num-i-1] = arr[num-i-1], arr[i]

    return arr
#end def


def min(arr):
    m = 0
    for el in arr:
        if m > el:
            m = el
    #end for

    return m
#end def

def sum(arr):
    s = 0
    for el in arr:
        s += el
    #end for

    return s
#end def

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    #end while 

    return a
#end def

def waga(n):
    suma = 0
    k = 2
    while n > 1 and k < n // 2:
        if n % k == 0:
            suma += 1
            while n % k == 0:
                n //= k
        k += 1
    return suma

def spr(t):
    suma = 0
    odw = [0] * len(t)
    for i in range(len(t)):
        odw[i] = waga(t[i])
        suma += odw[i]
    if suma % 3 == 0:
        if podzial(odw):
            return True
    else:
        return False

def podzial(t, n1=0, n2=0, n3=0, i=0):
    if i == len(t) :
        return n1 == n2 and n2 == n3
    return (t, n1 + t[i], n2, n3, i + 1) or (t, n1, n2 + t[i], n3, i + 1) or (t, n1, n2, n3 + t[i], i + 1)
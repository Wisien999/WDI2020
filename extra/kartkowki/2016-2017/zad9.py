# 1. Dwie liczby naturalne są „koleżankami” jeżeli mają przynajmniej dwie różne wspólne cyfry,
# np. 123 i 1345 lub 225 i 1235. Dana jest tablica t[N][N] wypełniona liczbami naturalnymi.
# Proszę napisać funkcję, która w tablicy t zeruje wszystkie liczby nie mające żadnej koleżanki.
# Do funkcji należy przekazać tablicę t. Funkcja powinna zwrócić ilość liczb naturalnych jaka
# pozostanie w tablicy.


def friends(n1, n2):
    digits = [False]*10

    while n1 > 0:
        digits[n1%10] = True
        n1 //= 10
    
    counter = 0

    while n2 > 0:
        if digits[n2%10] == True:
            digits[n2%10] = False
            counter += 1
        n2 //= 10

    return counter >= 2


def zero_not_friends(tab):
    for i1 in range(len(tab)*len(tab)):
        y1 = i1 // len(tab)
        x1 = i1 % len(tab[y1])

        have_friends = False

        for i2 in range(i1+1, len(tab)*len(tab)):
            y2 = i2 // len(tab)
            x2 = i2 % len(tab)

            if friends(tab[y1][x1], tab[y2][x2]):
                have_friends = True
                break
        
        if not have_friends:
            tab[y1][x1] = 0
        
    
    return tab


print(friends(234,2765))
print(friends(234,5))
print(friends(234,743))
print(friends(225,1235))
print(friends(123,1245))


from random import randint
n = 4
a = [[randint(1,200) for _ in range(n)] for _ in range(n)]

def print_tab(tab):
    for row in tab:
        for el in row:
            print(el, end="\t")
        print()
    print()

print_tab(a)
print_tab(zero_not_friends(a))
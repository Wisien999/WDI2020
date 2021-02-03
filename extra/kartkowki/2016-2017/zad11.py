# Dwie liczby naturalne są „przyjaciółkami” jeżeli zbiory cyfr z których zbudowane są liczby
# są identyczne. Na przykład: 123 i 321, 211 i 122, 35 i 3553. Dana jest tablica int t[N][N]
# wypełniona liczbami naturalnymi. Proszę napisać funkcję, która dla tablicy t zwraca ile
# elementów tablicy sąsiaduje wyłącznie z przyjaciółkami.


def friends(n1, n2):
    digits1 = [False]*10
    digits2 = [False]*10

    while n1 > 0:
        digits1[n1%10] = True
        n1 //= 10
    
    while n2 > 0:
        digits2[n2%10] = True
        n2 //= 10

    
    for i in range(10):
        if digits1[i] != digits2[i]:
            return False
    
    return True


# print(friends(123,321))
# print(friends(211,122))
# print(friends(35,3553))
# print(friends(453,854))


def count_neighbour_friends(tab):
    counter = 0

    moves = ((-1,0),(1,0),(0,1),(0,-1))

    for i in range(len(tab)*len(tab[0])):
        y = i // len(tab)
        x = i % len(tab[0])

        only = True
        for x_m, y_m in moves:
            if x+x_m >= 0 and x+x_m < len(tab[y]) and y+y_m >= 0 and y+y_m < len(tab):
                if not friends(tab[y][x], tab[y+y_m][x+x_m]):
                    only = False
                    break
        
        if only:
            print(tab[y][x])
            counter += 1
        
    print()
    return counter


n = 10

from random import randint
a = [[randint(1,10) for _ in range(n)] for _ in range(n)]

def print_tab(arr):
    for l in arr:
        for e in l:
            print(e, end="\t")
        print()
    print()

# a[0][0] = 5
# a[2][1] = 5
# a[1][0] = 5
# a[1][2] = 5
# a[0][1] = 5

print_tab(a)

print(count_neighbour_friends(a))

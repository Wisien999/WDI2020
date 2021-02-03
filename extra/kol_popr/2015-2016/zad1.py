# Zad. 1
# Dana jest tablica int t[N][N] zawierająca liczby naturalne. Dokładnie w jednym z wierszy
# tablicy znajduje się fragment ciągu Fibonacciego o długościwiększej niż2,a mniejszej niż N. Proszę
# napisać funkcję, która odszuka ten fragment ciągu i zwróci numer wiersza w którym on się znajduje.


def rev_fib(a, b):
    while a > 1 and b > 1:
        a, b = b-a, a

    return a == 1 and b == 2


def solve(arr):
    for i_l, line in enumerate(arr):
        for i in range(2, len(line)):

            if line[i] == line[i-1] + line[i-2]:
                
                if rev_fib(line[i-1], line[i]):
                    return i_l

    return False

arr = [[423,67,36,3,4,7], [234,5,8,13,21,423], [54,2346,2432,5234,23,4234]]

print(solve(arr))
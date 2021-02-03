# I zadanie (4 punkty)
# - dane są dwa ciągi określone następująco:
# a(1) = 1
# a(n) = a(n-1) + 2*b(n)
# b(1) = 2
# b(n) = b(n-1) + a(n-1)
# napisz funkcję, która przyjmie parametr k i zwróci n, dla którego różnica |b(n) - k| będzie najmniejsza,
# dla kilku identycznych różnic ma zwrócić numer pierwszego wyrazu


def solve(k):
    a, b = 1, 2
    best = float("inf")
    n = 1
    while True:
        n += 1
        b = b + a
        a = a + 2*b

        r = abs(b-k)
        # print(n, b, r, best)

        if r < best:
            best = r
        else:
            return n-1



print(solve(233544))
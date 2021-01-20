def solve(k):
    a, b = 1, 2
    la, lb = 1, 2
    i = 1
    bestA, bestB = -1, -1
    Ai, Bi = 1, 1

    while bestA < 0 or bestB < 0:
        print(i, " | ", a, b)
        if bestA < 0 and abs(k-la) < abs(k-a):
            bestA = abs(k-la)
            Ai = i-1

        if bestB < 0 and abs(k-lb) < abs(k-b):
            bestB = abs(k-lb)
            Bi = i-1


        la, lb = a, b
        b = b+a
        a = a + b/3
        i += 1

    if bestA < bestB:
        print("ciąg A nr", Ai)
    else:
        print("ciąg B nr", Bi)


solve(int(input()))
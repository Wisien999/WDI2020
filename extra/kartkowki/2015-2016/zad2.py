# 2) Proszę napisać program, który wypełnia tablicę t[N] pseudolosowymi liczbami nieparzystymi z zakresu [1..99],
# następnie Wyznacza i wypisuje różnicę pomiędzy długością najdłuższego znajdującego się w niej ciągu
# arytmetycznego o dodatniej różnicy, a długością najdłuższego ciągu arytmetycznego o ujemnej różnicy, przy
# założeniu, że kolejnymi wyrazami ciągu są elementy tablicy o kolejnych indeksach.

import random

def fill(n):
    return [random.randint(0, 49)*2 + 1 for _ in range(n)]

def find_arithmetic_subsequence(sequence, modificator):
    best = 1

    curr = 1

    r = (sequence[1] - sequence[0])*modificator

    for i in range(1, len(sequence)):
        rr = (sequence[i] - sequence[i-1])*modificator
        if rr == r and rr > 0:
            curr += 1
            # print("git", rr, curr)
        else:
            best = max(best, curr)
            curr = 2
            r = rr
            # print("not git", best, curr)
        
    return max(best, curr)



# arr = [2,3,4,11,6,1,-4]

# print(find_arithmetic_subsequence(arr, 1))
# print(find_arithmetic_subsequence(arr, -1))

def ex(n):
    t = fill(n)
    print(t)
    return find_arithmetic_subsequence(t, -1), find_arithmetic_subsequence(t, 1)

print(ex(5))
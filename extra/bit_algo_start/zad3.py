# Zadanie 2.1
# Mamy tablicę tab[N][N] wypełnioną cyframi(0-9). Chcemy znaleźć największą/najmniejszą liczbę
# utworzoną z 6 kolejnych cyfr leżących w jednym wierszu.
#  1 2 3 4 5 6 7 8 9
#  2 3 4 4 5 0 6 9 9


def solve(tab):

    def create_number(prev, new):
        return (prev%100000) * 10 + new
    
    maxi = 0
    mini = 10000000

    for y in range(len(tab)):
        num = 0
        for i in range(5):
            num = create_number(num, tab[y][i])
        print(num)    
        for x in range(5, len(tab[y])):
            num = create_number(num, tab[y][x])
            # print(num)
            
            maxi = max(maxi, num)
            mini = min(mini, num)
        
    return mini, maxi



arr = [
    [4,5,2,5,3,6,8,9,3,4,5],
    [4,5,2,5,3,6,8,9,3,4,5],
    [4,5,2,5,3,6,8,9,3,4,5],
    [4,5,2,5,3,6,8,9,3,4,5],
    [4,5,2,5,3,6,8,9,3,4,5],
    [4,5,2,5,3,6,8,9,3,4,5],
    [4,5,2,5,3,6,8,9,3,4,5],
    [4,5,2,5,3,6,8,9,3,4,5],
    [4,5,2,5,3,6,8,9,3,4,5]
]
print(solve(arr))
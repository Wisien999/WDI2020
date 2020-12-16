

def no_of_even_digits(num, base):
    if num == 0:
        return 1

    ans = 0

    while num > 0:
        ans += (num % base + 1) % 2
        num //= base

    return ans


def check(t1, t2, max1, max2, pos_x, pos_y):
    cells = 0
    good_cells = 0
    for x in range(max1):
        for y in range(max1):
            if x+pos_x < 0 or y+pos_y < 0 or x+pos_x >= max2 or y+pos_y >= max2:
                continue

            cells += 1

            if no_of_even_digits(t1[y][x], 5) == no_of_even_digits(t2[y+pos_y][x+pos_x], 5):
                good_cells += 1

    return good_cells/cells >= 33/100


def solve(t1, t2, max1, max2):
    for posx in range(-max1+1, max2):
        for posy in range(-max1+1, max2):
            if check(t1, t2, max1, max2, posx, posy):
                return True

    return False



# arr2 = [
#     [4,7,2,63],
#     [4,0,79,33],
#     [3,52,1,1],
#     [7,7,7,7]
# ]

arr2 = [
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]    
]

arr1 = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# print("ddd", no_of_even_digits(12,5))
print(solve(arr1,arr2,len(arr1),len(arr2)))
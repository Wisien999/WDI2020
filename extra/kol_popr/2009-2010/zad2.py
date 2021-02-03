def no_of_ones_in_bin(num):
    counter = 0
    while num > 0:
        counter += num%2
        num //= 2
    
    return counter


def solve(arr):
    for mask in range(3**len(arr)):
        am = [0]*3

        for i in range(len(arr)):
            am[mask%3] += no_of_ones_in_bin(arr[i])
            mask //= 3
        
        if am[0] == am[1] == am[2]:
            return True
    
    return False



arr = [2,3,5,7,15]
arr = [5,7,15]
print(solve(arr))

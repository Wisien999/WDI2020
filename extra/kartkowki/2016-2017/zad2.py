from time import sleep


def find(arr, k):
    greater = [0]*len(arr)
    smaller = [0]*len(arr)

    ans = [0]*k
    l = 0

    i = len(arr)

    while True:
        determinant = arr[i//2]
        i1 = 0
        i2 = 0

        same = 0

        for el in arr:
            if el > determinant:
                greater[i1] = el
                i1 += 1
            elif el < determinant:
                smaller[i2] = el
                i2 += 1
            elif el == determinant:
                same += 1
        
        print(arr, "arr")
        print(smaller, "smaller")
        print(greater, "greater")

        print(determinant)
        if i1 == k:
            print(i1, "=gr=k=", k)

            for el in greater:
                if el != 0:
                    ans[l] = el
                    l += 1

            return ans

        elif i1+same >= k >= i1:
            print(i1+same, "=gr+same >= k=", k, " >= gr=", k-1)
            for el in greater:
                if el != 0:
                    ans[l] = el
                    l += 1

            for _ in range(k-i1):
                ans[l] = determinant
                l += 1

            return ans
        
        elif i1 < k:
            print(i1, "=gr < k=", k)

            for el in greater:
                if el != 0:
                    ans[l] = el
                    l += 1
            print(l)
            
            for _ in range(same):
                ans[l] = determinant
                l += 1

            k -= i1 + same
            
            arr = smaller
            i = i2
        
        elif i1 > k:
            print(i1, "=g>k=", k)
            arr = greater
            i = i1
        
        greater = [0]*len(arr)
        smaller = [0]*len(arr)

        sleep(1)
        
        



import random

def solve(n):
    arr = [random.randint(1, 1000) for _ in range(n)]
    ans = find(arr, 10)
    print(ans)
    return sum(ans)



print(solve(50))

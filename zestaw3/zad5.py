def find_kth_smallest(tab, k):
    while True:
        determinant = tab[len(tab)//2]
        determinant = tab[0]
        smaller = []
        greater = []
        same = 0

        for el in tab:
        # for el in tab:
            if el < determinant:
                smaller.append(el)
            elif el == determinant:
                same += 1
            else:
                greater.append(el)
        
        # if len(smaller) < k:
        #     break


        # if len(smaller) == k:
        #     return max(smaller)
        # if len(smaller) == 0:
        #     tab = greater
        #     print("smaller empty", greater)
        if len(smaller) >= k:
            print("smaller", smaller)
            print("k", k, "     len smaller:", len(smaller))
            tab = smaller
        # elif len(tab) >= k:
        else:
            

            tab = greater + [determinant]*same
            print("greater", tab)
            print("old k:", k)
            k -= len(smaller)

            if len(smaller) == 0:
                if set(tab) == {determinant}:
                    return determinant
                tab = tab[:-same]
                k -= same

            print("new k:", k, "   len smaller:", len(smaller))
        # else:
        #     print("smaller", smaller)
        #     print("greater", greater)
        #     return determinant


        
        print("---------------------")
        if len(tab) <= 1:
            break
    
    # return sorted(tab)[k-1]

    return tab[0]



*seq, _ = map(int, input().split())

# seq = []
# while True:
#     a = int(input())
#     if a != 0:
#         break
#     seq.append(a)


print(seq)

k=10
sort = sorted(seq)
print(sort)
print(sort[k-1])
my = find_kth_smallest(seq, k)
print(my)
print(my == sort[k-1])

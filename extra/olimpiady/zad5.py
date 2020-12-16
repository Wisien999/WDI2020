def find(n, k):
    n_bin = ["0"]*(k-1) + list(bin(n)[2:])

    counter = 0
    for el in n_bin:
        if el == "1":
            counter += 1
            if counter >= k:
                return n
        else:
            counter = 0

    
    i = len(n_bin)-1

    while k > 0:
        k -= 1
        n_bin[i] = "1"
        i -= 1
    
    j = len(n_bin)-1
    while n_bin[i] == "1":
        n_bin[j] = "0"
        j -= 1
        i -= 1
    
    return int("".join(n_bin), 2)


n, k = map(int, input().split())
print(find(n, k))
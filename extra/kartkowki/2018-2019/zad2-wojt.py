if __name__ == "__main__":
    n = int(input())
    tab = [random.randint(1,10) for _ in range(n)]
    print(tab)
    result = 0
    result_elem = 0
    for k in range(len(tab)):
        result += k
    for elem in tab:
        result_elem += elem
    j = 0
    i = len(tab) - 1
    result2 = result
    result3 = result
    result_elem2 = result_elem
    result_elem3 = result_elem
    while i >= 0:
        if result - i == result_elem - tab[i]:
            print(i + 1)
            exit()
        i -= 1
    while j <= len(tab) - 1:
        if result2 - j == result_elem2 - tab[j]:
            print(len(tab)-j)
            exit()
        j += 1
    while i >= 0 and j <= len(tab) - 1:
        if result3 - j - i == result_elem - tab[i] - tab[j]:
            print(print(i-j))
            exit()
        i -= 1
        j += 1
    print("0")
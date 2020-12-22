#III zadanie (4 punkty)
#- duże liczby naturalne reprezentowane są w postaci napisów. Prosze napisać procedurę mnożącą
#dwie duże liczby naturalne. Do procedury należy przekazać mnożone liczby oraz parametr, w którym
#zwrócony bedzie wynik mnożenia. Można założyć, że każdy z czynników posiada nie wiecej niż 100
#cyfr

def add(n1, n2):
    res = [0]*max(len(n1)+1, len(n2)+1)

    i = 1
    for i in range(1, len(res)):
        if len(n1)-i >= 0:
            a = int(n1[len(n1)-i])
        else:
            a = 0
        
        if len(n2)-i >= 0:
            b = int(n2[len(n2)-i])
        else:
            b = 0

        res[len(res)-i] = a + b


    for i in range(len(res)-1, 0, -1):
        # print(res)
        res[i-1] += res[i]//10
        res[i] %= 10

    return res


# print(add("2345", "5008"))

# from time import sleep

def multiply(n1, n2):
    if len(n1) < len(n2):
        n1, n2 = n2, n1
    

    res = [0]*(len(n1)+2*len(n2))

    for i in range(1, len(n2)+1):
        tmp = [0]*(len(n1)+len(n2)+i)

        to_next = 0
        for j in range(1, len(n1)+1):
            tmp[len(tmp)-(j+i-1)] = int(n1[len(n1)-j]) * int(n2[len(n2)-i]) + to_next

            to_next = tmp[len(tmp)-(j+i-1)] // 10
            # print(to_next)
            tmp[len(tmp)-(j+i-1)] %= 10
            # print(tmp)
            # print(int(n1[len(n1)-j]), int(n2[len(n2)-i]))

            # sleep(0.5)
    
        
        # tmp = add(tmp, [0]*len(tmp))
        # print(tmp)
        res = add(res, tmp)
        # print(res)
    

    for i in range(len(res)):
        if res[i] != 0:
            break


    return "".join(map(str, res[i:]))






print(multiply("123456789", "987654321"))
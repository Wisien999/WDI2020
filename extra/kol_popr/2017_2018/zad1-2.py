def divide(T, c=1, i=0, suma=0):
    # sleep(0.1)
    # print(" "*i, c, i, suma)

    if i == len(T):
        return suma

    ans = divide(T, c + 1, i + 1, T[i])
    # print(" "*i, ans)
    
    if suma == ans:
        # print(" "*i, "git")
        return suma

    # print(" "*i, "nie git")

    ans = divide(T, c, i + 1, suma+T[i])
    # print(" "*i, "ans", ans)

    # if to_the_prev:
    #     print(" "*i, "cofaj")
    #     return ans


    # print(" "*i, "ostatnie")
    return ans



a = [1,2,3,1,5,2,2,2,6]
print(divide(a))

a = [3,3,1,7,6,1,2,2,2,1]
print(divide(a))
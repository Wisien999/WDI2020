def is_power_of_natural_number(num):
    if num == 1:
        return False
    

    components = {}

    i = 2
    while num > 1:
        while num % i == 0:
            components[i] = components.get(i, 0) + 1
            num //= i
        
        i += 1
    
    # print(components)

    pivot = components[list(components.keys())[0]]
    for component in components:
        if components[component] != pivot or components[component] < 2:
            return False
    
    return True


# print(is_power_of_natural_number(21))
# print(is_power_of_natural_number(64))
# print(is_power_of_natural_number(27))
# print(is_power_of_natural_number(36))
# print(is_power_of_natural_number(12))
# print(is_power_of_natural_number(22))


def ex1(t1, t2):
    sum1 = [t1[0]]
    for i in range(1, len(t1)):
        sum1.append(sum1[i-1]+t1[i])
    

    sum2 = [t2[0]]
    for i in range(1, len(t2)):
        sum2.append(sum2[i-1]+t1[i])
    
    sum_leng = 3
    for leng1 in range(1, sum_leng):
        leng2 = sum_leng - leng1

        for start1 in range(len(t1)-leng1):
            s1 = sum1[start1+leng1] - sum1[start1-1]
            # s1 = sum(t1[start1:start1+leng1])
            for start2 in range(len(t2)-leng2):
                s2 = sum2[start2+leng2] - sum2[start2-1]
                # s =  s1 + sum(t2[start2:start2+leng2])
                s = s1 + s2

                if is_power_of_natural_number(s):
                    return True
        
    return False

print(ex1([3,1,5,3,5,7], [4,61,3,5,3,5]))
import math

# possible multiple counts???


def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3 or num == 5:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    for i in range(6, int(math.sqrt(num))+1, 6):
        if num % (i-1) == 0 or num % (i+1) == 0:
            return False
        i += 2

    return True


def get_leng(num):
    return math.floor(math.log10(num)) + 1

def create_number(a, to_slice, leng_a, leng_to_slice, at):
    new_num = 0
    new_num += to_slice//(10**(leng_to_slice-at))
    new_num *= 10**leng_a
    new_num += a
    new_num *= 10**(leng_to_slice-at)
    new_num += to_slice%(10**(leng_to_slice-at))
    return new_num


print(get_leng(125032))
print(get_leng(1250340))
print(create_number(5,1234567,1,7,3))
print(create_number(52,1234567,2,7,3))
print(create_number(92,1234567,2,7,1))
print(create_number(17,1234567,2,7,0))

counter = 0
a, b = map(int, input().split())
# possible multiple counts???

for i in range(get_leng(a)):
    print(create_number(b, a, get_leng(b), get_leng(a), i))
    if is_prime(create_number(b, a, get_leng(b), get_leng(a), i)):
        counter += 1

for i in range(get_leng(b)):
    print(create_number(a, b, get_leng(a), get_leng(b), i))
    if is_prime(create_number(a, b, get_leng(a), get_leng(b), i)):
        counter += 1

print(counter)

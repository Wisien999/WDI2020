digits = [1,1,2,6,4,2,2,4,2,8]

def last_non_zero_digit(num):

    if num < 10:
        return digits[num]

    ten_digit = (num//10)%10
    if ten_digit % 2 == 1:
        return 4*last_non_zero_digit(num//5)*digits[num%10] % 10
    else:
        return 6*last_non_zero_digit(num//5)*digits[num%10] % 10
    
    return 0


n = int(input())

print(last_non_zero_digit(n))
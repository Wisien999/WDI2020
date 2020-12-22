import math

def opA(num):
    if int(math.log10(num)) + 1 >= 2:
        last_d = num%10
        one_before_last_d = (num%100)//10
        num //= 100
        num *= 10
        num += last_d
        num *= 10
        num += one_before_last_d
        
    return num


def opB(num):
    return num*3

def opC(num):
    leng = int(math.log10(num)) + 1
    # print("llll", leng)
    if leng >= 2:
        return num % (10**(leng-1))
    return num

# print(opC(542))

def rek(num, target, i=0, history = ""):
    # print(num, target, i, history)
    
    if num == target:
        # print(history)
        return history

    if i >= 7:
        return ""
    
    
    ans = rek(opA(num), target, i+1, history+"A")
    if ans:
        return ans
    
    ans = rek(opB(num), target, i+1, history+"B")
    if ans:
        return ans
    
    ans = rek(opC(num), target, i+1, history+"C")
    if ans:
        return ans
    
    return ""
    


print(rek(6, 3))

# a = 6
# print(a)
# a = opB(a)
# print("B", a)
# a = opA(a)
# print("A", a)
# a = opC(a)
# print("C", a)
# a = opB(a)
# print("B", a)
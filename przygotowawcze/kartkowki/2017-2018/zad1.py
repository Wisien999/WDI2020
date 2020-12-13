# Zadanie 1.
# Dwie liczby naturalne s¡ ró»nocyfrowe, je»eli nie posiadaj¡ »adnej wspólnej cyfry. Prosz¦ napisa¢ program,
# który wczytuje dwie liczby naturalne i poszukuje najmniejszej podstawy systemu (w zakresie 2-16), w którym
# liczby s¡ ró»nocyfrowe. Program powinien wypisa¢ znalezion¡ podstaw¦; je»eli podstawa taka nie istnieje,
# nale»y wypisa¢ komunikat o jej braku.
# Na przykaad: dla liczb 123 i 522 odpowiedzi¡ jest podstawa 11, bo 123 (10) = 102 (11) i 522 (10) = 435 (11)

def to_base(num, base):
    res = []
    
    while num > 0:
        res.append(num%base)
        num //= base

    return res  # nie ma znaczenia czy zwrócę liczbę czy jej rewers
    # return res[::-1]


def diff_digits(num1: list, num2: list):
    amount = [False]*16

    for digit in num1:
        amount[digit]  = True

    for digit in num2:
        if amount[digit]:
            return False
    
    return True



def check(num1, num2):
    for base in range(2, 16+1):
        n1, n2 = to_base(num1, base), to_base(num2, base)
        if diff_digits(n1, n2):
            print(base)
            return 
    
    print("NIE MA TAKIEJ PODSTAWY")
    

check(123,522)
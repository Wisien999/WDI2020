# Zadanie 1.1a (2017/2018)
# Dwie liczby naturalne są “różnocyfrowe”, jeżeli nie posiadają żadnej wspólnej cyfry. Proszę
# napisać program, który wczytuje dwie liczby naturalne i poszukuje najmniejszej podstawy
# systemu (w zakresie 2-16), w którym liczby są różnocyfrowe. Program powinien wypisać
# znalezione podstawy; jeżeli podstawa taka nie istnieje, należy wypisać komunikat o jej braku.
# Na przykład: dla liczb 123 i 522 odpowiedzią jest podstawa 11, bo 123(10) = 102(11) i 522(10) = 435(11)


def check(num1, num2, base):
    digits = [-1]*base
    i = 0

    while num1 > 0:
        if num1 % base in digits:
            num1 //= base
            continue

        digits[i] = num1 % base
        num1 //= base
    

    while num2 > 0:
        if num2 % base in digits:
            return False

        num2 //= base
    

    return True


def ex(num1, num2):
    for base in range(2, 17):
        if check(num1, num2, base):
            return base
    
    return "not found"


print(ex(123,1109345))
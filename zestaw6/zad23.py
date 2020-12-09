# Zadanie 23. Dana jest tablica T[N] zawierająca oporności N rezystorów wyrażonych całkowitą liczbą
# kΩ. Proszę napisać funkcję, która sprawdza czy jest możliwe uzyskanie wypadkowej rezystancji R (równej
# całkowitej liczbie kΩ) łącząc dowolnie 3 wybrane rezystory.


def zad(t, target):
    def rek(t, target, index=0, resistance=None, no_of_resistors=1, h=None):
        resistance = resistance or t[0]
        h = h or [(t[0], "first")]

        if no_of_resistors == 3:
            print(resistance, h, no_of_resistors)
            return abs(resistance - target) < 0.0001

        if index == len(t):
            return False
        
        
        return rek(t, target, index+1, resistance + t[index], no_of_resistors+1, [*h, (t[index], "szereg")]) or \
                rek(t, target, index+1, resistance, no_of_resistors, [*h]) or \
                rek(t, target, index+1, (resistance*t[index])/(resistance+t[index]), no_of_resistors+1, [*h, (t[index], "pararel")])

    return rek(t, target, 0, t[0], 1, [(t[0], "first")]) or \
        rek(t, target, 1, t[1], 1, [(t[1], "first")])


res = [3,6,2,4,2,6,2]
print(zad(res, 1.6))
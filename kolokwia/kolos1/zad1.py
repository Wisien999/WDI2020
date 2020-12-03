# Bartłomiej Wiśniewski
# Długość napisu wielokrotnego musi być podzielna przez długość napisu z którego powstał. Wystarczy więc szukać dzielników długości napisu i dla każdego
# sprawdzać czy to napis o tej długości tworzy napis wielokrotny

def multi(T):
    best = 0
    for word in T:
        leng = len(word)
        if leng < 2:
            continue

        div = leng-1

        while div > 0:
            if leng % div == 0:
                corr = True
                for i in range(leng):
                    if word[i] != word[i%div]:
                        corr = False
                        break
                if corr:
                    break
            
            div -= 1
        
        if corr:
            if best < len(word):
                best = len(word)

    return best
#end def

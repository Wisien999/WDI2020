# 2. W grze mag-mino wykorzystuje się klocki, które mają kształt prostokątów, na których obydwu końcach znajduje
# się liczba oczek od 0 do 9. Na każdym klocku z dwóch jego końców liczba oczek jest inna. W komplecie liczącym 90
# klocków do gry występują wszystkie kombinacje oczek i każda kombinacja występuje dokładnie jeden raz. Proszę
# napisać funkcję, która dla danego zbioru N klocków wyznacza najdłuższy ciąg jaki można z nich ułożyć.
# Na przykład dla zbioru 8 klocków: [2|8] [0|1] [2|3] [3|6] [2|6] [2|9] [3|4] [6|7]
# najdłuższy ciąg jaki można ułożyć ma długość 5 i ma postać : [8|2] [2|3] [3|6] [6|2] [2|9]
# Dane opisujące zestaw:
# const int N= ...
# struct klocek {
# int a;
# int b; // b>a
# };
# klocek zestaw[N];
# Do funkcji należy przekazać zestaw klocków, funkcja powinna zwrócić największą długość ciągu jaki można z tego zestawu zbudować.
# Wskazówka : kiedy z zestawu klocków da się zbudować ciąg?

class klocek:
    def __init__(self, a, b):
        self.a = min(a, b)
        self.b = max(a, b)



def divide_into_groups(parts):
    groups = [[] for _ in range(10)]

    for brick in parts:
        groups[brick.a].append(brick.b)
        groups[brick.b].append(brick.a)
    
    return groups


def find_the_longest_sequence(groups):
    def rek(groups, a, ignore, leng, h):
        best = leng
        for b in groups[a]:
            if (a, b) in ignore:
                continue
            
            ans = rek(groups, b, [*ignore, (a,b), (b,a)], leng+1, h+[(a,b)])
            best = max(best, ans)
            # if best < ans[0]:
            #     print(ans)
            #     best = ans[0]
        
        
        return best
    
    best = 0

    for i in range(10):
        ans = rek(groups, i,[], 0, [])
        best = max(best, ans)

    return best

def solve(bricks):
    g = divide_into_groups(bricks)
    # print(g)
    return find_the_longest_sequence(g)


arr = [klocek(2,8), klocek(0,1), klocek(2,3), klocek(3,6), klocek(2,6), klocek(2,9), klocek(3,4), klocek(6,7)]

print(solve(arr))
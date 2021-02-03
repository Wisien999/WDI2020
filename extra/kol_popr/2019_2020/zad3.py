# 3. Dane są deklarację reprezentujące listę z klockami mag-mina (patrz zadanie 2).
# struct klocek {
# int a;
# int b;
# klocek *next;
# };
# Lista zawiera zestaw klocków, które można ułożyć w ciąg. Niestety klocki pomieszały się. Proszę napisać funkcję,
# która ustawia klocki na liście w ciąg. Uwaga: orientacja klocków w liście jest właściwa.
# Na przykład listę: [2|9] [3|6] [8|2] [2|3] [6|2]
# należy przekształcić na listę: [8|2] [2|3] [3|6] [6|2] [2|9]

class Node:
    def __init__(self, a = None, b = None):
        self.a = a
        self.b = b
        self.next = None


def solve(l):
    
    def rek(l, curr, ignore, n, leng):
        if leng == n:
            curr.next = None
            return True

        # print_ll(curr)

        start = l
        while l != None:
            if l.a == curr.b and l not in ignore or curr.b == None:
                if rek(start, l, [*ignore, l], n, leng+1):
                    curr.next = l
                    return True
            l = l.next


        return False

    
    leng = len_ll(l)

    q = Node()
    q.next = l

    rek(l, q, [], leng, 0)
    # print_ll(q)
    return q

    # start = l
    # while l != None:
    #     if rek(start, l, [], leng, 1):
    #         return l
    #     l = l.next
    
    # return False


def len_ll(l):
    n = 0
    while l != None:
        n += 1
        l = l.next
    
    # print(n)
    return n


start = Node(2,9)
a = start
a.next = Node(3,6)
a = a.next
a.next = Node(8,2)
a = a.next
a.next = Node(2,3)
a = a.next
a.next = Node(6,2)

from helper_module import print_ll

print_ll(start)

# ans, start = solve(start)
print_ll(solve(start))

# print_ll(start)
        



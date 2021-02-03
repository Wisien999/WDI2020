# 3. Dana jest struktura Node opisująca listę jednokierunkową:
# struct Node { Node * next; int value; };
# Proszę zaimplementować funkcję Node* fixSortedList( Node* L ), która otrzymuje na
# wejściu listę jednokierunkową bez wartowanika. Lista ta jest prawie posortowana w tym sensie, że
# powstała z listy posortowanej przez zmianę jednego losowo wybranego elementu na losową
# wartość. Funkcja powinna przepiąć elementy listy tak, by lista stała się posortowana i zwrócić
# wskaźnik do głowy tej listy. Można założyć, że wszystkie liczby na liście są różne i że lista ma co
# najmniej dwa elementy. Funkcja powinna działać w czasie liniowym względem długości listy
# wejściowej.

from helper_module import Node, push_back


def find_spot(start, val):
    while start.next != None and start.next.val < val:
        start = start.next
    
    return start



def fixSortedList(ll):
    guardian = Node(next=ll)

    c = guardian.next

    while c.next != None:
        if c.next.val < c.val:

            smaller = c.next
            c.next = c.next.next

            smaller.next = None


            print(guardian)
            spot = find_spot(guardian, smaller.val)
            print(spot)

            q = spot.next
            smaller.next = q
            spot.next = smaller



            break
    
        c = c.next

    
    return guardian



from time import sleep
def print_ll(ll: Node):
    c = ll
    if ll.val == None:
        start = ll.next
        print(c.val, end="     ")
        c = c.next
    else:
        start = ll

    if c != None:
        print(c.val, end="     ")
        c = c.next

    while c != None and c != start:
        print(c.val, end="     ")
        c = c.next
    print()



from helper_module import arr2list

a = arr2list([1,2,3])
print(find_spot(a, 0))
print("\n")

t = [1,23,234,23564,37456,123456789,87654,99999,100000]
l = arr2list(t)
print(l)
print_ll(fixSortedList(l.next))

print()

t = [1, 2, 0, 4, 5, 6, 7, 8, 9, 10]
l = arr2list(t)
print(l)
print_ll(fixSortedList(l.next))

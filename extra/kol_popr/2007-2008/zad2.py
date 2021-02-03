# II zadanie (5 punktów)
# - dane są dwa łańcuchy odsyłaczowe (listy) zawierające uporządkowane rosnąco, niepowtarzające się
# liczby naturalne. Napisz procedurę, która przyjmie za parametry wskaźniki do pierwszych elementów
# dwóch list i usunie z nich powtarzające się elementy. Np. mając dane listy (1, 2, 3, 7, 8, 15, 23) oraz
# (2, 5, 6, 8, 13, 20, 23) ma usunąć z obu elementy: 2, 8, 23


def remove_common(l1, l2):
    while l1.next != None and l2.next != None:
        if l1.next.val > l2.next.val:
            l2 = l2.next
        elif l1.next.val < l2.next.val:
            l1 = l1.next
        else:
            q = l1.next
            l1.next = l1.next.next
            del q
            
            q = l2.next
            l2.next = l2.next.next
            del q
        
    

from helper_module import Node, arr2list

a = arr2list([3,46,78,345,4444])
b = arr2list([3,4,5,6,46,78,4444])

remove_common(a, b)

print(a)
print(b)
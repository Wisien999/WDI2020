# 2. Dane są dwie listy cykliczne powstałe przez zapętlenie listy jednokierunkowej posortowanej
# rosnąco, dla każdej listy dany jest wskaźnik wskazujący przypadkowy element w takiej liście.
# Proszę napisać funkcję, która dla dwóch list cyklicznych, usuwa z obu list elementy
# występujące w obu listach. Do funkcji należy przekazać wskaźniki na dwie listy, funkcja
# powinna zwrócić łączną liczbę usuniętych elementów.


# class Node:
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


def uncycle(c):
    """
    Return pointer to the element one before the first lement
    """

    while c.next.val > c.val:
        c = c.next
    
    start = Node(next=c.next)
    c.next = None

    return start



def remove_common(l1, l2):
    removed = 0

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
    
            removed += 1

    return removed



def solve(c1, c2):
    c1 = uncycle(c1)
    c2 = uncycle(c2)

    removed = remove_common(c1, c2)

    c1 = make_cycle(c1)
    c2 = make_cycle(c2)

    return removed


from helper_module import make_cycle, arr2list, print_ll, Node


a = make_cycle(arr2list([1,2,3,4,5,6]))
b = make_cycle(arr2list([0,5,6,7,8,9]))

print_ll(a)
print_ll(b)

print(solve(a, b))

print_ll(a)
print_ll(b)

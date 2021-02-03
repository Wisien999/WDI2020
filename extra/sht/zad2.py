# Zad.
# Dane są dwie listy równej długości. Napisz funkcję łączącą je w jedną elementami
# na przemian.

class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None


def push_back(l: Node, val: int):
    if l == None:
        return Node(val)


    while l.next != None:
        l = l.next
    
    l.next = Node(val)


def arr2list(arr: list):
    """
    Creates Linked List from Python list.
    Returned list has first node empty.
    """

    ans = Node()

    for el in arr:
        push_back(ans, el)
    
    return ans


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
        # if c.val =
        print(c.val, end="     ")
        c = c.next
    print()




def merge(l1: Node, l2: Node):
    if l1.val == None:
        l1 = l1.next
    if l2.val == None:
        l2 = l2.next

    ans = Node()
    ans_c = ans

    while l1 != None or l2 != None:
        if l1 != None:
            ans_c.next = l1
            ans_c = ans_c.next
            l1 = l1.next

        if l2 != None:
            ans_c.next = l2
            ans_c = ans_c.next
            l2 = l2.next

    return ans


a = arr2list([1,2,3,4,5,6])
b = arr2list([99,88,77,66,55,44])

print_ll(merge(a,b))
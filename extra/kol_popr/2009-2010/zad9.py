class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def divide_into_categories(l):
    ans = [Node() for _ in range(10)]
    i = [n for n in ans]

    if l.val == None:
        l = l.next

    while l != None:
        i[l.val%10].next = Node(l.val)
        
        i[l.val%10] = i[l.val%10].next
        l = l.next
    
    return ans


def combine(arr):
    ans = Node()
    c = ans

    for el in arr:
        if el.val == None:
            el = el.next

        c.next = el
        while c.next != None:
            c = c.next
    
    return ans

def solve(l):
    return combine(divide_into_categories(l))


import helper_module

a = helper_module.arr2list([3,4234,5,3,5,34,6,5,34,7,7,568,67,8,456,345,2,352])
helper_module.print_ll(a)
c = solve(a)
helper_module.print_ll(c)

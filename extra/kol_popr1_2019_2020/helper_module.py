
class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None


class Node_d:
    def __init__(self, value = None):
        self.val = value
        self.next = None
        self.prev = None


def print_ll(ll: Node):
    c = ll

    while c != None:
        # if c.val =
        print("[", c.a, "|", c.b, "]", end="     ")
        c = c.next
    print()


def print_back_ll(ll: Node):
    c = ll
    while c.next != None:
        c = c.next

    while c != None:
        print(c.val, end="      ")
        c = c.prev

    print()


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


def arr2dlist(arr: list):
    """
    Creates Doubly Linked List from Python list.
    Returned list has first node empty.
    """


    ans = Node_d()
    c = ans

    for el in arr:
        c.next = Node_d(el)
        # c = c.next
        c.next.prev = c
        c = c.next    
    
    return ans



def reverse_list(l: Node, ans: Node):
    """
    Reverses given list l and adds it to ans.
    "ans" must be Node object
    """

    if l.val == None:
        l = l.next

    while l != None:
        # if l.val == None:
        push_front(ans, l.val)
        l = l.next
    

    return ans
            
    
    # if l.next != None:
    #     reverse_list(l.next, ans)
    
    # if l.val != None:
    #     push_back(ans, l.val)


def push_front(l, val):
    q = Node(val)
    q.next = l.next
    l.next = q
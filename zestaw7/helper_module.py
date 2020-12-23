
class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None


def print_ll(ll: Node):
    c = ll
    while c != None:
        # if c.val =
        print(c.val, end="     ")
        c = c.next
    print()


def push_back(l: Node, val: int):
    if l == None:
        return Node(val)


    while l.next != None:
        l = l.next
    
    l.next = Node(val)



def arr2list(arr):
    ans = Node()

    for el in arr:
        push_back(ans, el)
    
    return ans



def reverse_list(l: Node, ans: Node):
    """
    Reverses given list l and adds it to ans.
    "ans" must be Node oject
    """
    
    if l.next != None:
        reverse_list(l.next, ans)
    
    if l.val != None:
        push_back(ans, l.val)


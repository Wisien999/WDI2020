# Zad.3
# Dany jest zbiór punktów płaszczyzny o współrzędnych będących liczbami całkowitymi.Zbior
# ten dany jest w postaci listy jednokierunkowej. Proszę funkcję, która rozdziela łańcuch na cztery
# łańcuchy zawierające punkty należące odpowiednio do l,ll,lll i lV ćwiartki układu współrzędnych,
# natomiast punkty leżące na osiach układu współrzędnych usuwa z pamięci. Proszę zadeklarować
# odpowiednie typy.


class Node:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
        self.next = None

    
def divide(ll):
    q1 = Node()
    q1c = q1
    q2 = Node()
    q2c = q2
    q3 = Node()
    q3c = q3
    q4 = Node()
    q4c = q4

    if ll.x == None:
        ll = ll.next

    
    while ll != None:
        next = ll.next
        ll.next = None

        if ll.x > 0 and ll.y > 0:
            q1c.next = ll
            q1c = q1c.next
        elif ll.x < 0 and ll.y > 0:
            q2c.next = ll
            q2c = q2c.next
        elif ll.x < 0 and ll.y < 0:
            q3c.next = ll
            q3c = q3c.next
        elif ll.x > 0 and ll.y < 0:
            q4c.next = ll
            q4c = q4c.next
        else:        
            del ll
        
        ll = next
        

    return q1, q2, q3, q4


from helper_module import print_xy, arr2xylist

a = arr2xylist([(3,6),(55,0), (-56,2),(-6,-2),(4,6),(-3,-3)])
res = divide(a)

for i in res:
    print_xy(i)
# 3. Kolejne (co najmniej dwa) elementy listy o identycznej wartości pola val nazywamy podlistą stałą. Proszę napisać
# funkcję, która usuwa z listy wejściowej najdłuższą podlistę stałą. Warunkiem jej usunięcia jest istnienie w liście
# dokładnie jednej najdłuższej podlisty stałej. Do funkcji należy przekazać wskaźnik na pierwszy element listy.
# Funkcja powinna zwrócić liczbę usuniętych elementów.
# Na przykład z listy [ 1 3 3 3 5 7 11 13 13 1 2 2 2 2 3 ] należy usunąć podlistę [ 2 2 2 2 ],
# a z listy [ 1 3 3 3 3 5 7 11 13 13 1 2 2 2 2 3 ] nie należy nic usuwać.


class Node:
    def __init__(self, val):
        self.val = val
        self.next = Node


def rm_longest_const_sublist(l):
    
    longest_leng = 0
    longest_prev = None
    longest_after = None


    c_leng = 0
    c_prev = l

    counter = 0

    while l.next != None:
        # print(c_leng)
        # print("current:", end="       ")
        # print_ll(c_prev, l.next)
        # print_ll(l)
        # sleep(1)

        if l.val != l.next.val:
            # print("not const")
            if c_leng > longest_leng:
                # print("new best", c_leng)
                longest_leng = c_leng
                longest_prev = c_prev
                longest_after = l.next
                
                
                counter = 0
            
            if c_leng == longest_leng:
                counter += 1

            c_leng = 0
            c_prev = l
        
        c_leng += 1
        l = l.next
    


    if c_leng > longest_leng:
        longest_leng = c_leng
        longest_prev = c_prev
        longest_after = l.next
        
        
        counter = 0
    
    if c_leng == longest_leng:
        counter += 1


    if counter == 1 and longest_leng >= 1:
        longest_prev.next = longest_after
        return longest_leng
    

    return 0
    



from helper_module import arr2list, print_ll
from time import sleep

a = arr2list([5,5,6,7,7,7,8])
print_ll(a)
print(rm_longest_const_sublist(a))
print_ll(a)


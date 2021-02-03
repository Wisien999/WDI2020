# 3. Dane są trzy listy jednokierunkowe uporządkowane rosnąco bez powtarzających się
# liczb. Proszę napisać funkcję która usunie w każdej liście elementy powtarzające się
# w trzech listach. Funkcja ma zwrócić liczbę usuniętych elementów.


def remove_common_3l(l1, l2, l3):
    counter = 0

    while l1.next != None and l2.next != None and l3.next != None:
        if l1.next.val > l2.next.val:
            l2 = l2.next
        elif l1.next.val < l2.next.val:
            l1 = l1.next
        else:
            val = l1.next.val
            while l3.next != None and l3.next.val < val:
                l3 = l3.next
            
            if l3.next != None and l3.next.val == val:
                q = l1.next
                l1.next = l1.next.next
                del q
    
                q = l2.next
                l2.next = l2.next.next
                del q
    
                q = l3.next
                l3.next = l3.next.next
                del q

                counter += 1
    

    return counter


from helper_module import Node, arr2list

a = arr2list([5,7,88,999,4555])
b = arr2list([5,8,9,4555,999999])
c = arr2list([1,2,5,6,7,88,65,4555])

print(remove_common_3l(a,b,c))

print(a)
print(b)
print(c)
# Zadanie 3.
# Dwie listy zawieraj¡ niepowtarzaj¡ce si¦ (w obr¦bie listy) liczby naturalne. W obu listach liczby s¡ posor-
# towane rosn¡co. Prosz¦ napisa¢ funkcj¦ usuwaj¡c¡ z ka»dej listy liczby wyst¦puj¡ce w drugiej. Do funkcji
# nale»y przekaza¢ wskazania na obie listy, funkcja powinna zwróci¢ a¡czn¡ list¦ usuni¦tych elementów.



def rm(l1, l2):
    removed = 0

    while l1.next != None and l2.next != None:
        if l1.next.val > l2.next.val:
            l2 = l2.next
        elif l1.next.val < l2.next.val:
            l1 = l1.next
        else:
            l1.next = l1.next.next
            l2.next = l2.next.next
            removed += 2
    
    return removed


from helper_module import arr2list, print_ll

a = arr2list([1,3,4,6,7,8,9])
b = arr2list([2,3,5,6,9])

print_ll(a)
print_ll(b)
print(rm(a, b))
print_ll(a)
print_ll(b)
